from PyQt5.QtWidgets import QTextEdit, QVBoxLayout

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class CommandPreview(AbstractPage):
    """Final wizard page to preview command before execute."""

    __layout = None
    __command_field = None

    def __init__(self):
        """
        Parameters:
        -----------
        command (str): Command to execute.
        """
        super().__init__()
        self.setTitle('Command preview')
        self.__layout = QVBoxLayout()
        self.__command_field = QTextEdit()
        self.setObjectName('command_preview_page')

    def create_page(self):
        self.__command_field.setReadOnly(True)
        self.__layout.addWidget(self.__command_field, 0)
        self.setLayout(self.__layout)

    def set_command(self, command):
        """Sets command

        Parameters:
        -----------

        command (str): Command to execute."""

        self.__command_field.setText(command)
