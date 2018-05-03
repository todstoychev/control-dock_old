from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QApplication

from Containers.Table import Table
from Containers.Toolbar import Toolbar
from Docker.Commands import Commands
from Icon import Icon


class Containers(QWidget):
    """
    Containers widget.

    Attributes:
        :__toolbar (Toolbar): Widget toolbar.
        :__table (Table): Containers list.
        :__show_all (QCheckBox): Show all containers checkbox.
        :__commands (Commands): Docker commands.
        :__app (QApplication): Application instance.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Containers')
        self.setWindowIcon(Icon())
        self.setLayout(QVBoxLayout())
        self.__toolbar = Toolbar()
        self.__table = Table()
        self.__show_all = QCheckBox()
        self.__commands = Commands()
        self.__app = QApplication.instance()

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
        self.__toolbar.stop_action.triggered.connect(self.__on_stop_action_clicked)
        self.__toolbar.restart_action.triggered.connect(self.__on_restart_action_clicked)
        self.__toolbar.delete_action.triggered.connect(self.__on_delete_action_clicked)
        self.__toolbar.terminal_action.triggered.connect(self.__on_terminal_action_clicked)
        self.__show_all.clicked.connect(self.__on_show_all_clicked)

    @pyqtSlot()
    def __on_start_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items_id(0)
        self.__commands.start_containers(containers)
        self.__table.set_data(self.__show_all.isChecked())
        self.__app.restoreOverrideCursor()

    @pyqtSlot()
    def __on_stop_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items_id(0)
        self.__commands.stop_containers(containers)
        self.__table.set_data(self.__show_all.isChecked())
        self.__app.restoreOverrideCursor()

    @pyqtSlot()
    def __on_restart_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items_id(0)
        self.__commands.restart_containers(containers)
        self.__table.set_data(self.__show_all.isChecked())
        self.__app.restoreOverrideCursor()

    @pyqtSlot()
    def __on_delete_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items_id(0)
        self.__commands.delete_containers(containers)
        self.__table.set_data(self.__show_all.isChecked())
        self.__app.restoreOverrideCursor()

    @pyqtSlot()
    def __on_show_all_clicked(self):
        checked = self.__show_all.isChecked()
        self.__table.set_data(show_all=checked)

    @pyqtSlot()
    def __on_terminal_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        containers = self.__table.get_selected_items_id(0)
        self.__commands.open_terminal(containers)
        self.__app.restoreOverrideCursor()
