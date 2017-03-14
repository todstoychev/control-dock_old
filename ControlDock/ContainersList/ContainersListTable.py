import re
import subprocess

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QAbstractItemView, QTableWidgetItem

from ControlDock.ApplicationStatus.ApplicationStatusBox import ApplicationStatusBox
from ControlDock.ListTable import ListTable


class ContainersListTable(ListTable):
    """Containers list table.

    Attributes:
        columns (list): Table columns list.
        table_data (list): Table row data.
        START_CONTAINER (str): Start container command.
        STOP_CONTAINER (str): Stop container command.
        DELETE_CONTAINER (str): Delete container command.
        RESTART_CONTAINER (str): Restart containers.
        OPERATION_TEXT (dict): Operation text messages."""

    START_CONTAINER = 'docker start '
    STOP_CONTAINER = 'docker stop '
    DELETE_CONTAINER = 'docker rm -f '
    RESTART_CONTAINER = 'docker restart '
    OPERATION_TEXT = {
        START_CONTAINER: 'Started container: ',
        DELETE_CONTAINER: 'Deleted container: ',
        STOP_CONTAINER: 'Stopped container: ',
        RESTART_CONTAINER: 'Restarted container: '
    }

    def __init__(self, *__args):
        super().__init__(*__args)

    def setup_table(self, show_all=False):
        """Setup table parameters

        Keyword arguments:
            show_all (bool): Filters all or only running containers."""
        self._get_data(show_all)
        self.setColumnCount(self.columns.__len__())
        self.setRowCount(self.table_data.__len__())
        self.setHorizontalHeaderLabels(self.columns)

        for row in range(0, self.table_data.__len__()):
            for i in range(0, self.table_data[row].__len__()):
                item = QTableWidgetItem(self.table_data[row][i])
                item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                self.setItem(row, i, item)

            self.setSelectionBehavior(QAbstractItemView.SelectRows)

    def containers_operation(self, operation=STOP_CONTAINER):
        """Stops running containers. Works with multiple table rows.

        Keyword arguments:
            operation (str): Operation command."""
        rows = self.selectionModel().selectedRows()

        if rows.__len__() == 0:
            self.show_warning_dialog('Please select at least one container to interact with it.')

        while True:
            rows = self.selectionModel().selectedRows()

            if rows.__len__() < 1:
                break

            row = rows[0]
            row_number = row.row()
            container_id = self.item(row_number, 0).text()
            container_name = self.item(row_number, 6).text()

            if container_name is None:
                container_name = container_id

            command = subprocess.Popen([operation + container_id], stdout=subprocess.PIPE, shell=True)
            (out, err) = command.communicate()

            if err is not None:
                self.show_err_dialog(err)

            self.removeRow(row_number)
            ApplicationStatusBox.prepend_status_text(self.OPERATION_TEXT[operation] + container_name + '\n')

    def _get_data(self, show_all=False):
        """Gets table data and fills up the table.

        Keyword arguments:
            show_all (bool): Show all containers flag"""
        self.columns = []
        self.table_data = []

        if show_all:
            show_all = ' -a'
        else:
            show_all = ''

        command = subprocess.Popen(['docker ps' + show_all], stdout=subprocess.PIPE, shell=True)
        (out, err) = command.communicate()
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

            if show_all and row.__len__() == 6:
                row.insert(5, 'N/A')

            self.table_data.append(row)
