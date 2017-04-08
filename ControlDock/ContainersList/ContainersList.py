import subprocess

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

from ControlDock.ApplicationStatus.ApplicationStatusBox import ApplicationStatusBox
from ControlDock.ContainersList.ContainersActions import ContainersActions
from ControlDock.ContainersList.ContainersListTable import ContainersListTable
from ControlDock.ContainersList.ShowAllCheckbox import ShowAllCheckbox
from ControlDock.WarningDialog import WarningDialog


class ContainersList(QWidget):
    """Containers list window."""

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setWindowTitle('Containers list')
        self.__table = ContainersListTable()
        self.__layout = QVBoxLayout()
        self.setMinimumWidth(740)
        self.__containers_actions = ContainersActions()
        self.__show_all_checkbox = ShowAllCheckbox()

    def create_ui(self):
        """Creates UI."""
        self.setLayout(self.__layout)
        self.__table.setup_table()
        self.__containers_actions.create_ui()
        self.__layout.addWidget(self.__table, 0)
        self.__layout.addWidget(self.__show_all_checkbox, 1)
        self.__layout.addLayout(self.__containers_actions, 1)

        # Define button actions
        self.__show_all_checkbox.clicked.connect(self.on_show_all_containers_checkbox_clicked)
        self.__containers_actions.stop_button.clicked.connect(self.on_stop_button_clicked)
        self.__containers_actions.delete_button.clicked.connect(self.on_delete_button_clicked)
        self.__containers_actions.start_button.clicked.connect(self.on_start_button_clicked)
        self.__containers_actions.refresh_button.clicked.connect(self.on_refresh_button_clicked)
        self.__containers_actions.open_shell_button.clicked.connect(self.on_open_shell_button_clicked)
        self.__containers_actions.restart_button.clicked.connect(self.on_restart_button_clicked)

        # Add status text
        ApplicationStatusBox.prepend_status_text('Containers list is loaded. \n')

    @pyqtSlot()
    def on_show_all_containers_checkbox_clicked(self):
        """Show all containers checkbox action"""
        show_all = False

        if self.__show_all_checkbox.isChecked():
            show_all = True

        self.setCursor(QCursor(Qt.BusyCursor))
        self.__table.setup_table(show_all)
        self.setCursor(QCursor(Qt.ArrowCursor))

        # Add status text
        ApplicationStatusBox.prepend_status_text('Containers list refreshed. \n')

    @pyqtSlot()
    def on_stop_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.containers_operation(self.__table.STOP_CONTAINER)
        self.__table.setup_table(self.__show_all_checkbox.isChecked())
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def on_delete_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.containers_operation(self.__table.DELETE_CONTAINER)
        self.__table.setup_table(self.__show_all_checkbox.isChecked())
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def on_start_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.containers_operation(self.__table.START_CONTAINER)
        self.__table.setup_table(self.__show_all_checkbox.isChecked())
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def on_refresh_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.setup_table(self.__show_all_checkbox.isChecked())
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))
        ApplicationStatusBox.prepend_status_text('Containers list refreshed. \n')

    @pyqtSlot()
    def on_open_shell_button_clicked(self):
        """Starts shell sessions in the selected containers."""
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        rows = self.__table.selectionModel().selectedRows()

        if rows.__len__() == 0:
            warning_dialog = WarningDialog()
            warning_dialog.create('Please select at least one container to interact with it.')

        for i in range(0, rows.__len__()):
            row = rows[i]
            row_number = row.row()
            container_id = self.__table.item(row_number, 0).text()
            container_name = self.__table.item(row_number, 6).text()
            cmd = ['x-terminal-emulator', '-e', 'docker exec -it ' + container_id + ' bash']
            subprocess.call(cmd)
            ApplicationStatusBox.prepend_status_text('Terminal session opened in  container: ' + container_name + '\n')

        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def on_restart_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.containers_operation(self.__table.RESTART_CONTAINER)
        self.__table.setup_table(self.__show_all_checkbox.isChecked())
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))
