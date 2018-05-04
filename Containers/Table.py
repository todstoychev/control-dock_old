from PyQt5.QtWidgets import QAbstractItemView

from BaseTable import BaseTable
from DateTimeFormatter import DateTimeFormatter


class Table(BaseTable):
    """
    Attributes:
       __columns (list): Column labels.
    """

    def __init__(self, *__args):
        super().__init__(*__args)

        self.__columns = ['ID', 'Name', 'Status', 'Image', 'Command', 'Ports', 'Created']

        self.setColumnCount(self.__columns.__len__())
        self.setHorizontalHeaderLabels(self.__columns)

    def set_data(self, show_all=False):
        containers = self._docker.containers.list(all=show_all)
        self.setRowCount(containers.__len__())
        row = 0

        for container in containers:
            container_id = container.short_id
            status = container.status
            name = container.name
            image = container.image.tags[0]
            command = self.__process_command(container.attrs['Config']['Cmd'])
            ports = self.__process_ports_dict(container.attrs['Config']['ExposedPorts'])
            created = DateTimeFormatter.format_string(container.attrs['Created'][0:-4], "%Y-%m-%dT%I:%M:%S.%f").strftime("%d.%m.%Y - %I:%m:%S")
            data = [container_id, name, status, image, command, ports, created]
            self._set_row_data(data, row)
            row += 1

        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.update()

    @staticmethod
    def __process_ports_dict(ports: dict):
        ports_string = ''

        for port in list(ports.keys()):
            ports_string += port + ' '

        return ports_string

    @staticmethod
    def __process_command(command_list: list):
        command = ''

        if type(command_list).__name__ != 'NoneType':
            for arg in command_list:
                command += ' '+arg

        return command

