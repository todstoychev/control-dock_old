from datetime import datetime

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView

from Docker.DockerFactory import DockerFactory


class Table(QTableWidget):
    """
    Attributes:
       __docker (docker): Docker client instance.
       __columns (list): Column labels.
    """

    def __init__(self, *__args):
        super().__init__(*__args)

        self.__docker = DockerFactory().create()
        self.__columns = ['Status', 'Name', 'Image', 'Command', 'Ports', 'Created']

        self.setColumnCount(self.__columns.__len__())
        self.setHorizontalHeaderLabels(self.__columns)

    def set_data(self, show_all=False):
        containers = self.__docker.containers(all=show_all)
        self.setRowCount(containers.__len__())
        row = 0

        for container in containers:
            status = container['Status']
            name = container['Names'][0].replace('/', '')
            image = container['Image']
            command = container['Command']
            ports = self.__process_ports_dict(container['Ports'])
            created = datetime.fromtimestamp(container['Created']).strftime("%d/%m/%Y - %H:%M:%S")
            data = [status, name, image, command, ports, created]
            self.__set_row_data(data, row)
            row += 1

        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.update()

    def __set_row_data(self, data: list, row: int):
        index = 0

        for item in data:
            self.setItem(row, index, QTableWidgetItem(item))
            index += 1

    @staticmethod
    def __process_ports_dict(ports: list):
        ports_string = ''

        for port in ports:
            ports_string += port['Type'] + '/' + port['PrivatePort'].__str__()

            if port is not ports[ports.__len__() - 1]:
                ports_string += ', '

        return ports_string

    def get_selected_containers_names(self):
        """
        Returns containers names from selected table rows.

        :return list: List of selected containers names.
        """
        selection = self.selectedItems()
        containers = []

        for item in selection:
            if item.column() is 2:
                containers.append(item.text())

        return containers
