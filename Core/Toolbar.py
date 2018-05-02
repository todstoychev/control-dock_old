from functools import partial
import qtawesome
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QAction

from Containers.Containers import Containers
from Images.Images import Images


class Toolbar(QToolBar):
    """
    Attributes:
        __mdi QMdiArea: Mdi widget.
    """
    __CONTAINERS = 'containers'
    __IMAGES = 'images'

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setMovable(False)

    def create_ui(self):
        containers = QAction(QIcon(qtawesome.icon('fa.list')), 'Containers', self)
        containers.setToolTip('Containers list.')
        containers.triggered.connect(partial(self.__on_action_clicked, self.__CONTAINERS))
        self.addAction(containers)

        images = QAction(QIcon(qtawesome.icon('fa.database')), 'Images', self)
        images.setToolTip('Images list.')
        images.triggered.connect(partial(self.__on_action_clicked, self.__IMAGES))
        self.addAction(images)

    @pyqtSlot()
    def __on_action_clicked(self, identifier: str):
        instance = None

        if identifier == self.__CONTAINERS:
            instance = Containers

        if identifier == self.__IMAGES:
            instance = Images

        mdi = self.parent().centralWidget()
        found = mdi.findChildren(instance)

        if found.__len__() < 1:
            found = instance()
            found.create_ui()
            mdi.addSubWindow(found)
            found.show()

            return

        found[0].setWindowState(Qt.WindowActive)
