import subprocess

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

from ControlDock.ApplicationStatus.ApplicationStatusBox import ApplicationStatusBox
from ControlDock.ContainerWizard.ContainerWizard import ContainerWizard
from ControlDock.ImagesList.ImageListTable import ImageListTable
from ControlDock.ImagesList.ImagesActions import ImagesActions


class ImagesList(QWidget):
    """Images list widget.

    Attributes:
        __table (ImageListTable): List table.
        __layout (QVBoxLayout): Layout.
        __images_actions (ImagesActions): Images actions.4
        __container_wizard (ContainerWizard): Container wizard."""

    __table = None
    __layout = None
    __images_actions = None
    __container_wizard = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Available images list')
        self.setMinimumWidth(540)
        self.__table = ImageListTable()
        self.__layout = QVBoxLayout()
        self.__images_actions = ImagesActions()
        self.setLayout(self.__layout)

    def create_ui(self):
        """Creates widget UI."""
        self.__table.setup_table()
        self.__layout.addWidget(self.__table)
        self.__images_actions.create_ui()
        self.__layout.addLayout(self.__images_actions)

        # Define slots
        self.__images_actions.refresh_button.clicked.connect(self.on_refresh_images_list_button_clicked)
        self.__images_actions.delete_button.clicked.connect(self.on_delete_images_button_clicked)
        self.__images_actions.start_button.clicked.connect(self.on_start_container_button_clicked)

    @pyqtSlot()
    def on_refresh_images_list_button_clicked(self):
        self.setCursor(QCursor(Qt.BusyCursor))
        app = QApplication.instance()
        self.__table.setup_table()
        app.processEvents()
        self.setCursor(QCursor(Qt.ArrowCursor))
        ApplicationStatusBox.prepend_status_text('Images list refreshed. \n')

    @pyqtSlot()
    def on_delete_images_button_clicked(self):
        """Stops running containers. Works with multiple table rows."""
        rows = self.__table.selectionModel().selectedRows()

        if rows.__len__() == 0:
            self.__table.show_warning_dialog('Please select at least one image to interact with it.')

        while True:
            rows = self.__table.selectionModel().selectedRows()

            if rows.__len__() < 1:
                break

            row = rows[0]
            row_number = row.row()
            image_id = self.__table.item(row_number, 2).text()
            image_name = self.__table.item(row_number, 0).text()
            command = subprocess.Popen(['docker rmi ' + image_id], stdout=subprocess.PIPE, shell=True)
            (out, err) = command.communicate()

            if err is not None:
                self.__table.show_err_dialog(err)

            self.__table.removeRow(row_number)
            ApplicationStatusBox.prepend_status_text('Deleted image: ' + image_name + '\n')

    @pyqtSlot()
    def on_start_container_button_clicked(self):
        """Start the container build widget."""
        rows = self.__table.selectionModel().selectedRows()

        if rows.__len__() == 0:
            self.__table.show_warning_dialog('Please select at least one image to interact with it.')

            return

        if rows.__len__() > 1:
            self.__table.show_warning_dialog('Please select only one image to interact with.')

            return

        row = rows[0]
        row_number = row.row()
        row_data = {
            'image_id': self.__table.item(row_number, 2).text(),
            'repository': self.__table.item(row_number, 0).text(),
            'tag': self.__table.item(row_number, 1).text()
        }
        self.__container_wizard = ContainerWizard(row_data)
        parent = self.parentWidget()
        parent = parent.parentWidget()
        parent = parent.parentWidget()
        parent.addSubWindow(self.__container_wizard)
        self.__container_wizard.create_ui()
        self.__container_wizard.show()
