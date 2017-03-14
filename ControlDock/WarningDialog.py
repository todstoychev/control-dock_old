import logging
from PyQt5.QtWidgets import QMessageBox
from ControlDock.Log import Log
from ControlDock.WindowIcon import WindowIcon


class WarningDialog:
    """Create warning message dialog."""

    def __init__(self):
        self.__window_icon = WindowIcon.get_icon()

    def create(self, message, window_icon=None, write_log=False):
        """Creates the error message dialog.

            Attributes:
                message (str): Error message text.

            Keyword arguments:
                window_icon (PyQt5.QtGui.QIcon) Icon object.
                write_log (bool) Write log message."""
        dialog = QMessageBox()
        dialog.setWindowIcon(self.__window_icon)

        if window_icon is not None:
            dialog.setWindowIcon(window_icon)

        dialog.setText(message)
        dialog.setIcon(QMessageBox.Warning)
        dialog.setWindowTitle("Warning")
        dialog.exec_()

        if write_log is True:
            log = Log(logging.WARNING)
            log.write(message)
