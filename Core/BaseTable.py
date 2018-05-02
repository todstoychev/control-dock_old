from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget

from Docker.DockerFactory import DockerFactory


class BaseTable(QTableWidget):
    """
    Base table object, used to construct some of the application tables that share common logic.

    Attributes:
        :_docker (docker): Docker client instance.
    """

    def __init__(self, *__args):
        super().__init__(*__args)

        self._docker = DockerFactory().create()

    def _set_row_data(self, data: list, row: int):
        """
        Adds data to table row.

        :param data: Data to add.
        :param row: Row number.
        :return:
        """
        index = 0

        for item in data:
            print(item)
            self.setItem(row, index, QTableWidgetItem(item))
            index += 1

    def get_selected_items_id(self, column_number: int):
        """
        Gets selected items identificators, using column number to point to the identification data.

        :param column_number: Column number, where object identificators is.
        :return (list): List of identificators.
        """
        selection = self.selectedItems()
        items = []

        for item in selection:
            if item.column() is column_number:
                items.append(item.text())

        return items
