import qtawesome
from PyQt5.QtWidgets import QToolBar, QAction


class Toolbar(QToolBar):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.__start_action = QAction(qtawesome.icon('fa.play'), 'Start', self)
        self.__delete_action = QAction(qtawesome.icon('fa.trash'), 'Delete', self)

    def create_ui(self):
        self.__start_action.setToolTip('Create Docker container from Docker image.')
        self.addAction(self.__start_action)

        self.__delete_action.setToolTip('Deletes Docker images.')
        self.addAction(self.__delete_action)

    @property
    def start_action(self):
        return self.__start_action

    @property
    def delete_action(self):
        return self.__delete_action
