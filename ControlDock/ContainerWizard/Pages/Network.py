from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QLabel, QTextEdit

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class Network(AbstractPage):
    """Network settings page.

    Attributes:
        __layout (QGridLayout): Base layout for this page.
        __ports_label (QLabel): Port mappings text field label.
        port_mappings (QTextEdit): Port mappings field."""

    __layout = None
    __ports_label = None
    port_mappings = None

    def __init__(self):
        super().__init__()
        self.__layout = QGridLayout()
        self.__ports_label = QLabel('Port mappings')
        self.port_mappings = QTextEdit()
        self.setObjectName('network_page')

    def create_page(self):
        """Creates page."""

        self.setTitle('Network settings')
        self.setSubTitle('Network setting for your container.')
        self.setLayout(self.__layout)

        self.port_mappings.setPlaceholderText('Use docker command syntax to add the mappings. For example: '
                                              'host:container. Add only one pair per line')
        self.port_mappings.setMaximumHeight(100)

        self.__layout.addWidget(self.__ports_label, 0, 0, Qt.AlignTop)
        self.__layout.addWidget(self.port_mappings, 0, 1)
