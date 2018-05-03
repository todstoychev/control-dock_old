from PyQt5.QtWidgets import QAbstractItemView

from BaseTable import BaseTable


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
            id = container.short_id
            status = container.status
            name = container.name
            image = container.image.tags[0]
            command = container.attrs['Args'].__str__()
            ports = self.__process_ports_dict(container.attrs['Config']['ExposedPorts'])
            created = container.attrs['Created']
            data = [id, name, status, image, command, ports, created]
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
            ports_string += port+' '

        return ports_string
