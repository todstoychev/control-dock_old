import qtawesome
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QToolBar, QAction

from Containers.Containers import Containers


class Toolbar(QToolBar):
    """
    Attributes:
        __mdi QMdiArea: Mdi widget.
    """

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setMovable(False)

    def create_ui(self):
        containers = QAction(QIcon(qtawesome.icon('fa.list')), 'Containers', self)
        containers.setToolTip('Containers list.')
        containers.triggered.connect(self.on_containers_clicked)
        self.addAction(containers)

    @pyqtSlot()
    def on_containers_clicked(self):
        mdi = self.parent().centralWidget()
        containers = mdi.findChildren(Containers)

        if containers.__len__() < 1:
            containers = Containers()
            containers.create_ui()
            mdi.addSubWindow(containers)
            containers.show()

            return

        containers[0].setWindowState(Qt.WindowActive)
