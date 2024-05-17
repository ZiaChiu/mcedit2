"""
    pending_imports
"""
from __future__ import absolute_import, division, print_function, unicode_literals
from PySide6 import QtWidgets, QtCore
import logging

log = logging.getLogger(__name__)

class PendingImportsWidget(QtWidgets.QWidget):
    def __init__(self):
        super(PendingImportsWidget, self).__init__()
        self.importsListWidget = QtWidgets.QListView()
        self.importsListModel = QtCore.QStandardItemModel()
        self.importsListWidget.setModel(self.importsListModel)
        self.importsListWidget.clicked.connect(self.listClicked)
        self.importsListWidget.doubleClicked.connect(self.listDoubleClicked)
