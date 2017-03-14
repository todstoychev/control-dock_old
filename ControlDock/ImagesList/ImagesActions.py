from PyQt5.QtWidgets import QGridLayout

from ControlDock.Buttons.DeleteButton import DeleteButton
from ControlDock.Buttons.RefreshButton import RefreshButton
from ControlDock.Buttons.StartButton import StartButton


class ImagesActions(QGridLayout):
    """Images actions layout.

    Attributes:
        refresh_button (RefreshButton): Refresh button."""

    refresh_button = None

    def __init__(self):
        super().__init__()
        self.refresh_button = RefreshButton()
        self.delete_button = DeleteButton()
        self.start_button = StartButton()

    def create_ui(self):
        """Creates UI."""
        self.setColumnStretch(1, 200)
        self.refresh_button.setToolTip('Refreshes images list.')
        self.refresh_button.setObjectName('refresh_images_list_button')
        self.delete_button.setToolTip('Deletes images from your computer.')
        self.delete_button.setObjectName('delete_images_button')
        self.start_button.setToolTip('Starts container from selected image.')
        self.start_button.setObjectName('start_container_button')

        self.addWidget(self.refresh_button, 0, 2)
        self.addWidget(self.delete_button, 0, 0)
        self.addWidget(self.start_button, 0, 3)
