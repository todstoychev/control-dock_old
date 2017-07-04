import qtawesome
from PyQt5.QtWidgets import QToolBar, QAction


class Toolbar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)
        self.__start_action = QAction(qtawesome.icon('fa.play'), 'Start', self)

    def create_ui(self):
        self.setToolTip('Create docker container from docker image.')
        self.addAction(self.__start_action)

    @property
    def start_action(self):
        return self.__start_action
