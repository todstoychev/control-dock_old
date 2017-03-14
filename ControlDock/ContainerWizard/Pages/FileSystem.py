from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QTextEdit

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class FileSystem(AbstractPage):
    """File system mounts.

    Attributes:
            __layout (QGridLayout): Base layout for this page.
            __ports_label (QLabel): Port mappings text field label.
            port_mappings (QTextEdit): Port mappings field."""

    __layout = None
    __volumes_label = None
    filesystem_mappings = None

    def __init__(self):
        super().__init__()
        self.__layout = QGridLayout()
        self.__volumes_label = QLabel('Filesystem mappings')
        self.filesystem_mappings = QTextEdit()
        self.setObjectName('filesystem_page')

    def create_page(self):
        """Creates page."""

        self.setTitle('Volumes mappings')
        self.setSubTitle('Filesystem mounts.')
        self.setLayout(self.__layout)

        self.filesystem_mappings.setPlaceholderText('Use docker command syntax to add the mappings. For example: '
                                                    'host:container. Add only one pair per line')
        self.filesystem_mappings.setMaximumHeight(100)

        self.__layout.addWidget(self.__volumes_label, 0, 0, Qt.AlignTop)
        self.__layout.addWidget(self.filesystem_mappings, 0, 1)
