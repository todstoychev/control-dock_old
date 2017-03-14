import subprocess

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QWizard

from ControlDock.ContainerWizard.CommandBuilder import CommandBuilder
from ControlDock.ContainerWizard.Pages.CommandPreview import CommandPreview
from ControlDock.ContainerWizard.Pages.ContainerStartOptions import ContainerStartOptions
from ControlDock.ContainerWizard.Pages.FileSystem import FileSystem
from ControlDock.ContainerWizard.Pages.Network import Network
from ControlDock.ContainerWizard.Pages.Result import Result


class ContainerWizard(QWizard):
    """Creates and runs docker container with certain configuration.

    Attributes:
        image_id (str): Docker image id.
        __tag (str): Image tag/version.
        __repository (str): Image repository.
        container_identification (ContainerStartOptions): Container identification page.
        command_preview (CommandPreview): Command preview page.
        command_builder (CommandBuilder): Command builder.
        network (Network): Network settings page.
        filesystem (FileSystem): Filesystem mappings.
        result (Result): Result page."""

    image_id = ''
    __tag = ''
    __repository = ''
    container_identification = None
    command_preview = None
    command_builder = None
    network = None
    filesystem = None
    result = None

    def __init__(self, row):
        """Intializes object.

        Parameters:
        -----------
            :param row (list): Docker image id."""

        super().__init__()
        self.container_identification = ContainerStartOptions()
        self.command_preview = CommandPreview()
        self.network = Network()
        self.filesystem = FileSystem()
        self.command_builder = CommandBuilder('docker run -d ')
        self.setWindowTitle('Run container')
        self.image_id = row['image_id']
        self.__repository = row['repository']
        self.__tag = row['tag']
        self.result = Result()

    def create_ui(self):
        """Creates UI."""
        self.addPage(self.container_identification)
        self.addPage(self.network)
        self.addPage(self.filesystem)
        self.addPage(self.command_preview)
        self.addPage(self.result)
        self.container_identification.create_page(self.__repository, self.__tag)
        self.network.create_page()
        self.filesystem.create_page()
        self.command_preview.create_page()

        # Define slots
        next_button = self.button(QWizard.NextButton)
        next_button.clicked.connect(self.on_next_button_clicked)
        finish_button = self.button(QWizard.FinishButton)
        finish_button.clicked.connect(self.on_finish_button_clicked)
        cancel_button = self.button(QWizard.CancelButton)
        cancel_button.clicked.connect(self.on_cancel_button_clicked)

    @pyqtSlot()
    def on_next_button_clicked(self):
        current_page = self.currentPage()

        if current_page.objectName() == 'command_preview_page':
            # Build command
            self.command_builder.container_name(self.container_identification.name_field.text())
            self.command_builder.host_name(self.container_identification.host_name_field.text())
            self.command_builder.ports(self.network.port_mappings.toPlainText())
            self.command_builder.filesystem(self.filesystem.filesystem_mappings.toPlainText())

            self.command_preview.set_command(
                self.command_builder.build_command(self.image_id, self.__repository, self.__tag)
            )

        if current_page.objectName() == 'result_page':
            self.setCursor(QCursor(Qt.BusyCursor))
            app = QApplication.instance()
            command = subprocess.Popen([self.command_builder.command], stdout=subprocess.PIPE, shell=True)
            (out, err) = command.communicate()
            out = out.__str__()
            container_id = ''

            if len(out) > 4:
                container_id = out
                container_id = container_id.replace('b', '')

            self.result.create_page(container_id)
            app.processEvents()
            self.setCursor(QCursor(Qt.ArrowCursor))

    @pyqtSlot()
    def on_finish_button_clicked(self):
        self.parent().close()

    @pyqtSlot()
    def on_cancel_button_clicked(self):
        self.parent().close()
