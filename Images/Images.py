from PyQt5.QtWidgets import QWidget, QVBoxLayout

from Icon import Icon
from Images.Table import Table
from Images.Toolbar import Toolbar


class Images(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Images')
        self.setWindowIcon(Icon())
        self.setLayout(QVBoxLayout())
        self.__toolbar = Toolbar()
        self.__table = Table()

    def create_ui(self):
        self.__toolbar.create_ui()

        self.layout().addWidget(self.__toolbar)
        self.layout().addWidget(self.__table)

        self.__table.set_data()
        self.setMinimumWidth(self.__table.width())
