from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextEdit


class ApplicationStatusBox(QTextEdit):
    """Custom text edit field used as operation log message box."""

    def __init__(self, text=None):
        """Keyword arguments:
            text (str): Initial text in the box."""
        super().__init__()
        self.setText(text)
        self.__cursor = self.textCursor()
        self.setReadOnly(True)
        self.setMinimumHeight(200)
        self.setMinimumWidth(200)
        self.setObjectName('application_status_box')

    def prepend(self, text):
        """Prepends text in the text box.

        Parameters
        ----------
        text : str
            Text to prepend

        Keyword arguments:
            color (str): Text color"""
        self.__cursor.movePosition(QTextCursor.Start)
        self.__cursor.insertText(text)

    @staticmethod
    def prepend_status_text(text):
        """Finds itself and prepends text to it.

        Parameters
        ----------
        text (str): Message text."""
        app = QApplication.instance()
        application_status_box = app.activeWindow().findChild(ApplicationStatusBox, 'application_status_box')

        if application_status_box is not None:
            application_status_box.prepend(text)
