import logging
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from ControlDock.Log import Log
from ControlDock.WindowIcon import WindowIcon


class ErrorDialog:
    """Create error message dialog."""

    def __init__(self):
        self.__window_icon = WindowIcon.get_icon()

    def create(self, message, window_icon=None):
        """Creates the error message dialog.

            Attributes:
                message (str): Error message text.

            Keyword arguments:
                window_icon (PyQt5.QtGui.QIcon) Icon object."""
        dialog = QMessageBox()
        dialog.setWindowIcon(self.__window_icon)

        if window_icon is not None:
            dialog.setWindowIcon(window_icon)

        dialog.setText(message)
        dialog.setIcon(QMessageBox.Critical)
        dialog.setWindowTitle("Error")
        dialog.buttonClicked.connect(self.close_app)
        dialog.exec_()

        log = Log(logging.CRITICAL)
        log.write(message)

    @staticmethod
    def close_app():
        """Closes the application on dialog button click."""
        QApplication(sys.argv).instance().exit(1)
