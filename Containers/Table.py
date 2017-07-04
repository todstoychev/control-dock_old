from datetime import datetime

from PyQt5.QtWidgets import QAbstractItemView

from BaseTable import BaseTable


class Table(BaseTable):
    """
    Attributes:
       __columns (list): Column labels.
    """

    def __init__(self, *__args):
        super().__init__(*__args)

        self.__columns = ['Status', 'Name', 'Image', 'Command', 'Ports', 'Created']

        self.setColumnCount(self.__columns.__len__())
        self.setHorizontalHeaderLabels(self.__columns)

    def set_data(self, show_all=False):
        containers = self._docker.containers(all=show_all)
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

    @staticmethod
    def __process_ports_dict(ports: list):
        ports_string = ''

        for port in ports:
            ports_string += port['Type'] + '/' + port['PrivatePort'].__str__()

            if port is not ports[ports.__len__() - 1]:
                ports_string += ', '

        return ports_string
