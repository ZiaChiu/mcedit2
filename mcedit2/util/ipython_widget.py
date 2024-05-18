"""
    ipython_widget
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import os

from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager
from IPython.lib import guisupport
from PySide6 import QtWidgets

log = logging.getLogger(__name__)

# TODO: ipython.lib.gui_support does not support pyside6 or qt 6
# TODO: from the QT documentation to find a way replace gui_support

def print_process_id():
    print('Process ID is:', os.getpid())

def terminal_widget(**kwargs):

    # Create an in-process kernel
    # >>> print_process_id()
    # will print the same process ID as the main process
    kernel_manager = QtInProcessKernelManager()
    kernel_manager.start_kernel()
    kernel = kernel_manager.kernel
    kernel.gui = 'qt'
    kernel.shell.push(kwargs)

    kernel_client = kernel_manager.client()
    kernel_client.start_channels()

    control = RichJupyterWidget()
    control.kernel_manager = kernel_manager
    control.kernel_client = kernel_client
    return control

def main():
    # Print the ID of the main process
    print_process_id()

    app = QtWidgets.QApplication([])
    control = terminal_widget(testing=123)

    def stop():
        control.kernel_client.stop_channels()
        control.kernel_manager.shutdown_kernel()
        app.exit()

    control.exit_requested.connect(stop)

    control.show()

    guisupport.start_event_loop_qt6(app)

if __name__ == '__main__':
    main()
