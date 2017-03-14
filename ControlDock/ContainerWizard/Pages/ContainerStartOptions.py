from PyQt5.QtWidgets import QFormLayout, QGridLayout, QLabel, QLineEdit, QHBoxLayout

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class ContainerStartOptions(AbstractPage):
    """Container identification wizard page.

    Attributes:
        __layout (QGridLayout): Page layout.
        __name_label (QLabel): Name field label.
        __host_label (QLabel): Host name field label.
        name_field (QLineEdit): Container name field.
        host_name_field (QLineEdit): Host name field."""

    __layout = None
    __name_label = None
    __host_label = None
    __image_label = None
    __tag_label = None
    repository_field = None
    tag_field = None
    name_field = None
    host_name_field = None

    def __init__(self):
        super().__init__()
        self.__layout = QFormLayout()
        self.__name_label = QLabel('Name')
        self.name_field = QLineEdit()
        self.setTitle('Container identification')
        self.setSubTitle('Input your container identification data as container name and etc.')
        self.__host_label = QLabel('Host name')
        self.host_name_field = QLineEdit()
        self.setObjectName('container_start_options_page')
        self.__image_label = QLabel('Image')
        self.__tag_label = QLabel(':')
        self.repository_field = QLineEdit()
        self.tag_field = QLineEdit()

    def create_page(self, repository='', tag=''):
        """Creates wizard page.

        Keyword arguments:
            :argument repository: Image repository.
            :argument tag: Image tag/version."""
        self.setLayout(self.__layout)

        # Image field
        self.repository_field.setToolTip('Docker image repository.')
        self.repository_field.setPlaceholderText('Repository')
        self.repository_field.setText(repository)
        self.tag_field.setToolTip('Docker image tag/version.')
        self.tag_field.setPlaceholderText('Tag')
        self.tag_field.setText(tag)
        image_field_layout = QHBoxLayout()
        image_field_layout.addWidget(self.repository_field)
        image_field_layout.addWidget(self.__tag_label)
        image_field_layout.addWidget(self.tag_field)
        self.__layout.addRow(self.__image_label, image_field_layout)

        # Creates container name field composition
        self.name_field.setToolTip('Human readable container name (--name).')
        self.name_field.setPlaceholderText('Container name')
        self.__layout.addRow(self.__name_label, self.name_field)

        # Host name
        self.host_name_field.setToolTip('Container host name (--hostname).')
        self.host_name_field.setPlaceholderText('Host name')
        self.__layout.addRow(self.__host_label, self.host_name_field)
