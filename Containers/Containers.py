from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox

from Containers.Table import Table
from Containers.Toolbar import Toolbar
from Docker.Commands import Commands
from Icon import Icon


class Containers(QWidget):
    __toolbar = None
    __table = None
    __show_all = None
    __commands = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Containers')
        self.setWindowIcon(Icon())
        self.setLayout(QVBoxLayout())
        self.__toolbar = Toolbar()
        self.__table = Table()
        self.__show_all = QCheckBox()
        self.__commands = Commands()

    def create_ui(self):
        self.__show_all.setToolTip('Show all containers including stopped.')
        self.__show_all.setText('Show all containers')

        self.__toolbar.create_ui()
        self.__table.set_data()

        self.layout().addWidget(self.__toolbar)
        self.layout().addWidget(self.__table)
        self.layout().addWidget(self.__show_all)

        self.setMinimumWidth(self.__table.width())

        self.__toolbar.start_action.triggered.connect(self.__on_start_action_clicked)
        self.__show_all.clicked.connect(self.__on_show_all_clicked)

    @pyqtSlot()
    def __on_start_action_clicked(self):
        selection = self.__table.selectedItems()

        containers = []

        for item in selection:
            if item.column() is 2:
                containers.append(item.text())

        self.__commands.start_containers(containers)
        self.__table.set_data(self.__show_all.isChecked())

    @pyqtSlot()
    def __on_show_all_clicked(self):
        checked = self.__show_all.isChecked()
        self.__table.set_data(show_all=checked)
