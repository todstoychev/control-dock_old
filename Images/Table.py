from datetime import datetime

from PyQt5.QtWidgets import QAbstractItemView

from BaseTable import BaseTable


class Table(BaseTable):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.__columns = ['Repository', 'Id', 'Size', 'Created']

        self.setColumnCount(self.__columns.__len__())
        self.setHorizontalHeaderLabels(self.__columns)

    def set_data(self):
        images = self._docker.images()
        self.setRowCount(images.__len__())
        row = 0

        for image in images:
            created = datetime.fromtimestamp(image['Created']).strftime("%d/%m/%Y - %H:%M:%S")
            size = ((image['Size'] / 1024) / 1024)

            if size > 1000:
                size = size / 1024
                size = round(size, 2).__str__() + 'GB'
            else:
                size = round(size, 2).__str__() + 'MB'

            data = [
                image['RepoTags'][0],
                image['Id'],
                size,
                created
            ]
            self.__set_row_data(data, row)
            row += 1

        self.resizeColumnsToContents()
        self.setSortingEnabled(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.update()
