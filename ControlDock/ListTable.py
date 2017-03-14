import abc

from PyQt5.QtWidgets import QTableWidget

from ControlDock.ErrorDialog import ErrorDialog
from ControlDock.WarningDialog import WarningDialog


class ListTable(QTableWidget):
    """Base list table class.

    Attributes:
        columns (list): Holds table column names.
        table_data (list): Holds table data."""

    columns = []
    table_data = []

    def __init__(self, *__args):
        super().__init__(*__args)

    @staticmethod
    def show_err_dialog(message):
        """Static method to show error dialog message if something went wrong during the operations.
            Arguments:
                message (str): Message text
        """
        error_dialog = ErrorDialog()
        error_dialog.create(message)

    @staticmethod
    def show_warning_dialog(message):
        """Shoes warning dialog.

        Properties
        ----------
        message (str): Text to show."""
        warning_dialog = WarningDialog()
        warning_dialog.create(message)

    @abc.abstractmethod
    def _get_data(self):
        raise NotImplementedError('Class must define _get_data method.')

    @abc.abstractmethod
    def setup_table(self):
        raise NotImplementedError('Class must implement setup_table method.')
