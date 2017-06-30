import qtawesome
from PyQt5.QtWidgets import QToolBar, QAction


class Toolbar(QToolBar):
    __start_action = None

    def __init__(self, *__args):
        super().__init__(*__args)

    def create_ui(self):
        self.__start_action = QAction(qtawesome.icon('fa.play'), 'Start', self)
        self.__start_action.setToolTip('Start container')
        self.__start_action.setObjectName('start_container')
        self.addAction(self.__start_action)

    @property
    def start_action(self):
        return self.__start_action
