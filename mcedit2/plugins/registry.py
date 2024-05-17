from __future__ import absolute_import, division, print_function, unicode_literals
import logging

from PySide6 import QtCore

log = logging.getLogger(__name__)


class PluginClassRegistry(QtCore.QObject):
    pluginRemoved = QtCore.Signal(object)
    pluginAdded = QtCore.Signal(object)

    pluginClass = NotImplemented

    def __init__(self):
        super(PluginClassRegistry, self).__init__()
        self.pendingRegistrations = []
        self.registeredPlugins = []

    def commitRegistrations(self):
        for cls in self.pendingRegistrations:
            self.registeredPlugins.append(cls)
            self.pluginAdded.emit(cls)
        self.pendingRegistrations[:] = []

    def registerClass(self, cls):
        if issubclass(cls, self.pluginClass):
            self.pendingRegistrations.append(cls)
        else:
            raise ValueError("Class %s must inherit from %s" % (cls, self.pluginClass))
        return cls

    def unregisterClass(self, cls):
        if issubclass(cls, self.pluginClass):
            self.pluginRemoved.emit(cls)
            # TODO: check if it affects running
            if cls in self.registeredPlugins:
                self.registeredPlugins.remove(cls)
