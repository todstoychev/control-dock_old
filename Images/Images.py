from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QMessageBox

from Docker.Commands import Commands
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
        self.__commands = Commands()
        self.__app = QApplication.instance()

    def create_ui(self):
        self.layout().addWidget(self.__toolbar)
        self.layout().addWidget(self.__table)

        self.__toolbar.create_ui()
        self.__table.set_data()
        self.setMinimumWidth(self.__table.width())

        self.__toolbar.delete_action.triggered.connect(self.__on_delete_action_clicked)
        self.__toolbar.start_action.triggered.connect(self.__on_start_action_clicked)

    @pyqtSlot()
    def __on_delete_action_clicked(self):
        self.__app.setOverrideCursor(Qt.BusyCursor)
        images = self.__table.get_selected_items_id(1)
        self.__commands.delete_images(images)
        self.__table.set_data()
        self.__app.restoreOverrideCursor()

    @pyqtSlot()
    def __on_start_action_clicked(self):
        msg = QMessageBox()
        msg.setInformativeText('Functionality under construction!')
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Warning')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(msg.close)
        self.parent().parent().parent().addSubWindow(msg)
        msg.show()
