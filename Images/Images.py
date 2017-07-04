from PyQt5.QtCore import pyqtSlot
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
        self.layout().addWidget(self.__toolbar)
        self.layout().addWidget(self.__table)

        self.__toolbar.create_ui()
        self.__table.set_data()
        self.setMinimumWidth(self.__table.width())

    @pyqtSlot()
    def __on_delete_action_clicked(self):
        pass
