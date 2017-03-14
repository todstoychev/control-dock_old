import os

from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QToolBar

from ControlDock.ContainersList.ContainersList import ContainersList
from ControlDock.ImagesList.ImagesList import ImagesList


class NavigationToolbar(QToolBar):
    """Navigation toolbar.

    Attributes:
        :param path (str) Current path."""

    path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, *__args):
        super().__init__(*__args)

    def create_ui(self):
        """Creates UI."""
        self.__create_containers_list_action()
        self.__create_images_list_action()

    @pyqtSlot()
    def on_containers_list_triggered(self):
        """Containers list slot. Performs action to show containers list sub window."""
        parent_widget = self.parentWidget()
        containers_list = parent_widget.findChildren(ContainersList, 'containers_list_widget')

        if len(containers_list) > 0:
            containers_list[0].setWindowState(Qt.WindowNoState)
            containers_list[0].setFocus()

            return

        containers_list = ContainersList()
        containers_list.setObjectName('containers_list_widget')
        containers_list.create_ui()
        parent_widget.mdi.addSubWindow(containers_list)
        containers_list.show()

    @pyqtSlot()
    def on_images_list_triggered(self):
        parent_widget = self.parentWidget()
        images_list = parent_widget.findChild(ImagesList, 'images_list_widget')

        if images_list is not None:
            images_list.setWindowState(Qt.WindowNoState)
            images_list.setFocus()

            return

        images_list = ImagesList()
        images_list.setObjectName('images_list_widget')
        images_list.create_ui()
        parent_widget.mdi.addSubWindow(images_list)
        images_list.show()

    def __create_containers_list_action(self):
        """Creates containers list action."""
        containers_list = QAction(QIcon(self.path + '/../resources/icons/16x16/list.png'), 'Show containers list.',
                                  self)
        containers_list.setObjectName('containers_list')
        containers_list.triggered.connect(self.on_containers_list_triggered)
        self.addAction(containers_list)

    def __create_images_list_action(self):
        """Creates images list action."""
        images_list = QAction(QIcon(self.path + '/../resources/icons/16x16/iso.png'), 'Show available images list.',
                              self)
        images_list.setObjectName('images_list')
        images_list.triggered.connect(self.on_images_list_triggered)
        self.addAction(images_list)
