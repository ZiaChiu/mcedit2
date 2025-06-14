"""
    configureblocksdialog.py
"""
from __future__ import absolute_import, division, print_function
import json
import logging
import os
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt

from mcedit2.ui.dialogs.configure_blocks import Ui_configureBlocks
from mcedit2.util.directories import getUserFilesDirectory
from mcedit2.widgets.blocktype_list import TexturePixmap

log = logging.getLogger(__name__)


class BlockDefinition(object):
    def __init__(self, internalName=None, defJson=None):
        super(BlockDefinition, self).__init__()
        assert internalName or defJson, "Need at least one of internalName or defJson to create BlockDefinition"
        if defJson is None:
            defJson = {}
        self.internalName = internalName or defJson['internalName']
        self.rotationFlags = defJson.get('rotationFlags', [])
        self.meta = defJson.get('meta', 0)
        self.opacity = defJson.get('opacity', 15)
        self.brightness = defJson.get('brightness', 0)
        self.unlocalizedName = defJson.get('unlocalizedName', internalName)
        self.englishName = defJson.get('englishName', internalName)
        self.modelPath = defJson.get('modelPath', None)
        self.modelRotations = defJson.get('modelRotations', [0, 0])
        self.modelTextures = defJson.get('modelTextures', {})

    def exportAsJson(self):
        keys = ['internalName',
                'rotationFlags',
                'meta',
                'opacity',
                'brightness',
                'unlocalizedName',
                'englishName',
                'modelPath',
                'modelRotations',
                'modelTextures']

        d = {}
        for key in keys:
            d[key] = getattr(self, key)

        return d


class ConfigureBlocksItemDelegate(QtWidgets.QStyledItemDelegate):
    pass

class TextureListModel(QtCore.QAbstractListModel):
    def __init__(self, resourceLoader):
        super(TextureListModel, self).__init__()
        self.resourceLoader = resourceLoader
        self.textureNames = list(resourceLoader.blockTexturePaths())
        self.texturePixmaps = {}

    def zipfilePaths(self):
        zips = set()
        for zipFilename, _ in self.textureNames:
            if zipFilename in zips:
                continue
            zips.add(zipFilename)
            yield zipFilename

    def rowCount(self, parent):
        if parent.isValid():
            return 0
        return len(self.textureNames)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return

        row = index.row()
        zipFilename, texturePath = self.textureNames[row]
        if role == Qt.DisplayRole:
            return texturePath.rsplit("/", 1)[-1]
        if role == Qt.DecorationRole:
            pixmap = self.texturePixmaps.get(texturePath)
            if pixmap:
                return pixmap

            f = self.resourceLoader.openStream(texturePath)
            pixmap = TexturePixmap(f, 48, texturePath)
            self.texturePixmaps[texturePath] = pixmap
            return pixmap
        if role == self.TexturePathRole:
            return texturePath
        if role == self.ZipfilePathRole:
            return zipFilename

    TexturePathRole = Qt.UserRole
    ZipfilePathRole = Qt.UserRole + 1


class ConfigureBlocksItemModel(QtCore.QAbstractItemModel):

    def __init__(self, *args, **kwargs):
        super(ConfigureBlocksItemModel, self).__init__(*args, **kwargs)
        self.headerTitles = ["Icon",
                             "Block ID",
                             "Rotation Flags",
                             "Meta",
                             "Opacity",
                             "Brightness",
                             "Unlocalized Name",
                             "Name"]

        definedBlocksFilename = "defined_blocks.json"
        self.definedBlocksFilePath = os.path.join(getUserFilesDirectory(), definedBlocksFilename)
        try:
            definedBlocks = json.load(open(self.definedBlocksFilePath, "r"))
        except (ValueError, EnvironmentError) as e:
            log.warning("Failed to read definitions file %s", definedBlocksFilename)
            definedBlocks = []
        if not isinstance(definedBlocks, list):
            definedBlocks = []
        self.definedBlocks = []

        for defJson in definedBlocks:
            try:
                self.definedBlocks.append(BlockDefinition(defJson=defJson))
            except (KeyError, ValueError) as e:
                log.warning("Failed to load a definition from %s: %r", definedBlocksFilename, e)

    def exportAsJson(self):
        defs = []
        for blockDef in self.definedBlocks:
            defs.append(blockDef.exportAsJson())
        return defs

    def writeToJson(self):
        with open(self.definedBlocksFilePath, "w") as f:
            json.dump(self.exportAsJson(), f)

    def headerData(self, column, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Vertical:
            return None
        if role == Qt.DisplayRole:
            return self.headerTitles[column]
        return None

    def columnCount(self, index):
        return len(self.headerTitles)

    def rowCount(self, index):
        if index.isValid():
            return 0
        return len(self.definedBlocks)

    def index(self, row, column, parent=QtCore.QModelIndex()):
        if parent.isValid():
            return QtCore.QModelIndex()

        return self.createIndex(row, column, None)

    def parent(self, index):
        return QtCore.QModelIndex()

    COL_ICON = 0
    COL_ID = 1
    COL_ROTATION = 2
    COL_META = 3
    COL_OPACITY = 4
    COL_BRIGHTNESS = 5
    COL_UNLOCALIZED = 6
    COL_ENGLISH = 7

    def flags(self, index):
        if not index.isValid():
            return 0

        flags = QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if index.column() in (self.COL_ID,
                              self.COL_META,
                              self.COL_OPACITY,
                              self.COL_BRIGHTNESS,
                              self.COL_UNLOCALIZED,
                              self.COL_ENGLISH,
                              ):
            flags |= Qt.ItemIsEditable

        return flags

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()
        blockDef = self.definedBlocks[row]
        if role == Qt.DisplayRole:
            if column == self.COL_ICON:
                return None
            if column == self.COL_ID:
                return blockDef.internalName
            if column == self.COL_ROTATION:
                return blockDef.rotationFlags
            if column == self.COL_META:
                return blockDef.meta
            if column == self.COL_OPACITY:
                return blockDef.opacity
            if column == self.COL_BRIGHTNESS:
                return blockDef.brightness
            if column == self.COL_UNLOCALIZED:
                return blockDef.unlocalizedName
            if column == self.COL_ENGLISH:
                return blockDef.englishName
            return None
        return None

    def setData(self, index, value, role=Qt.DisplayRole):
        row = index.row()
        column = index.column()
        block_def = self.definedBlocks[row]
        if role == Qt.EditRole:
            try:
                if column == self.COL_ID:
                    block_def.internalName = value
                if column == self.COL_META:
                    block_def.meta = int(value)
                if column == self.COL_OPACITY:
                    block_def.opacity = int(value)
                if column == self.COL_BRIGHTNESS:
                    block_def.brightness = int(value)
                if column == self.COL_UNLOCALIZED:
                    block_def.unlocalizedName = value
                if column == self.COL_ENGLISH:
                    block_def.englishName = value
            except ValueError:
                log.exception("ValueError in setData")
                return False

            self.dataChanged.emit(index, index)
            return True

        return False

    def addBlock(self, internalName):
        log.info("Adding block %s", internalName)
        blockDef = BlockDefinition(internalName)
        self.beginInsertRows(QtCore.QModelIndex(), len(self.definedBlocks), len(self.definedBlocks))
        self.definedBlocks.append(blockDef)
        log.info("Appended")
        self.endInsertRows()

    def removeBlock(self, row):
        if row >= len(self.definedBlocks):
            return
        self.beginRemoveRows(QtCore.QModelIndex(), row, row)
        del self.definedBlocks[row]
        self.endRemoveRows()

    def setBlockModelPath(self, row, model_path):
        block_def = self.definedBlocks[row]
        block_def.modelPath = model_path


class ConfigureBlocksDialog(QtWidgets.QDialog, Ui_configureBlocks):
    def __init__(self, parent):
        super(ConfigureBlocksDialog, self).__init__(parent)
        self.setupUi(self)
        self.okButton.clicked.connect(self.accept)

        self.texListNameProxyModel = None
        self.texListZipProxyModel = None

        self.model = ConfigureBlocksItemModel()
        self.itemDelegate = ConfigureBlocksItemDelegate()

        self.blocksView.setModel(self.model)
        self.blocksView.setItemDelegate(self.itemDelegate)

        self.blocksView.clicked.connect(self.currentBlockClicked)

        self.internalNameBox.editTextChanged.connect(self.nameTextChanged)
