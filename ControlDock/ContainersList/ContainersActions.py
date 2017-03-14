from PyQt5.QtWidgets import QGridLayout

from ControlDock.Buttons.DeleteButton import DeleteButton
from ControlDock.Buttons.OpenShellButton import OpenShellButton
from ControlDock.Buttons.RefreshButton import RefreshButton
from ControlDock.Buttons.RestartButton import RestartButton
from ControlDock.Buttons.StartButton import StartButton
from ControlDock.Buttons.StopButton import StopButton


class ContainersActions(QGridLayout):
    """Containers buttons holder.

    Attributes:
        delete_button (DeleteButton): Delete button object.
        stop_button (StopButton): Stop button object.
        refresh_button (RefreshButton): Refresh button object.
        start_button (StartButton): Start button object.
        open_shell_button (OpenShellButton): Open shell to image."""

    def __init__(self):
        super().__init__()
        self.setColumnStretch(2, 200)
        self.delete_button = DeleteButton()
        self.stop_button = StopButton()
        self.refresh_button = RefreshButton()
        self.start_button = StartButton()
        self.open_shell_button = OpenShellButton()
        self.restart_button = RestartButton()

    def create_ui(self):
        """Creates the UI."""
        self.delete_button.setToolTip('Delete containers.')
        self.delete_button.setObjectName('delete_containers_button')
        self.open_shell_button.setObjectName('open_shell_button')
        self.open_shell_button.setToolTip('Opens shell sessions to containers.')
        self.refresh_button.setObjectName('refresh_containers_button')
        self.refresh_button.setToolTip('Refreshes running containers list.')
        self.start_button.setObjectName('start_containers_button')
        self.start_button.setToolTip('Starts stopped containers.')
        self.stop_button.setToolTip('Stops running containers.')
        self.stop_button.setObjectName('stop_containers_button')
        self.restart_button.setToolTip('Restarts containers.')
        self.restart_button.setObjectName('restart_container_button')

        self.addWidget(self.delete_button, 0, 1)
        self.addWidget(self.stop_button, 0, 0)
        self.addWidget(self.restart_button, 0, 4)
        self.addWidget(self.open_shell_button, 0, 3)
        self.addWidget(self.refresh_button, 0, 5)
        self.addWidget(self.start_button, 0, 6)
