import qtawesome
from PyQt5.QtWidgets import QToolBar, QAction


class Toolbar(QToolBar):
    """
    Containers window toolbar.

    Attributes:
        :__start_action (QAction):
        :__stop_action (QAction):
        :__restart_action (QAction):
        :__delete_action (QAction):
        :__terminal_action (QAction):
    """

    def __init__(self, *__args):
        super().__init__(*__args)
        self.__start_action = QAction(qtawesome.icon('fa.play'), 'Start', self)
        self.__stop_action = QAction(qtawesome.icon('fa.stop'), 'Stop', self)
        self.__restart_action = QAction(qtawesome.icon('fa.refresh'), 'Restart', self)
        self.__delete_action = QAction(qtawesome.icon('fa.trash'), 'Delete', self)
        self.__terminal_action = QAction(qtawesome.icon('fa.terminal'), 'Terminal', self)

    def create_ui(self):
        # Start action
        self.__start_action.setToolTip('Start container')
        self.addAction(self.__start_action)

        # Stop action
        self.__stop_action.setToolTip('Stops running containers.')
        self.addAction(self.__stop_action)

        # Restart action
        self.__restart_action.setToolTip('Restart containers.')
        self.addAction(self.__restart_action)

        # Delete action
        self.__delete_action.setToolTip('Force deletes container.')
        self.addAction(self.__delete_action)

        # Terminal action
        self.__terminal_action.setToolTip('Open terminal session to containers.')
        self.addAction(self.__terminal_action)

    @property
    def start_action(self):
        return self.__start_action

    @property
    def stop_action(self):
        return self.__stop_action

    @property
    def restart_action(self):
        return self.__restart_action

    @property
    def delete_action(self):
        return self.__delete_action

    @property
    def terminal_action(self):
        return self.__terminal_action
