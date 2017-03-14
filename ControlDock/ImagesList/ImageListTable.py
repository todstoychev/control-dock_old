import re
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem

from ControlDock.ListTable import ListTable


class ImageListTable(ListTable):
    """Images list."""

    def __init__(self, *__args):
        super().__init__(*__args)

    def setup_table(self):
        self.columns = []
        self.table_data = []

        self._get_data()
        self.setColumnCount(self.columns.__len__())
        self.setRowCount(self.table_data.__len__())
        self.setHorizontalHeaderLabels(self.columns)

        for row in range(0, self.table_data.__len__()):
            for i in range(0, self.table_data[row].__len__()):
                item = QTableWidgetItem(self.table_data[row][i])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.setItem(row, i, item)

            self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def _get_data(self):
        """Gets table data."""
        command = subprocess.Popen(['docker images'], stdout=subprocess.PIPE, shell=True)
        (out, err) = command.communicate()

        if err is not None:
            self.__show_err_dialog(err)

        rows = out.splitlines()

        for i in range(0, rows.__len__()):
            row = rows[i].__str__()
            row = re.sub(r"^b\'", '', row)
            row = re.sub(r"\'$", '', row)
            row = re.split(r'\s{2,}', row)

            if i == 0:
                for col in row:
                    self.columns.append(col.lower().capitalize())

                continue

            self.table_data.append(row)
