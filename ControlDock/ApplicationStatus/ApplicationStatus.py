from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDockWidget

from ControlDock.ApplicationStatus.ApplicationStatusBox import ApplicationStatusBox


class ApplicationStatus(QDockWidget):
    """Application log box."""

    def __init__(self, *__args):
        super().__init__(*__args)
        self.application_status_box = ApplicationStatusBox()
        self.application_status_box.append('Welcome to Control Dock!')
        self.setWidget(self.application_status_box)
        self.setMaximumHeight(150)
        self.setWindowTitle('Status')
        self.setObjectName('application_status_widget')
        self.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.setFloating(True)
