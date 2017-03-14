from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QMdiArea

from ControlDock.ApplicationStatus.ApplicationStatus import ApplicationStatus
from ControlDock.MenuBarActions.QuitAction import QuitAction
from ControlDock.MenuBarActions.ShowApplicationStatusWidgetAction import ShowApplicationStatusWidgetAction
from ControlDock.NavigationToolbar import NavigationToolbar
from ControlDock.WindowIcon import WindowIcon


class MainWindow(QMainWindow):
    """Main window.

    Attributes:
        mdi (QMdiArea): Mdi area.
        navigation_toolbar (NavigationToolbar): Navigation toolbar."""

    def __init__(self):
        super().__init__()
        self.mdi = QMdiArea()
        self.navigation_toolbar = NavigationToolbar()
        self.application_status = ApplicationStatus()
        self.menu_bar = self.menuBar()
        self.setWindowTitle('Control Dock')
        self.setWindowIcon(WindowIcon.get_icon())

    def create_ui(self):
        """Creates UI."""
        self.setCentralWidget(self.mdi)
        self.addToolBar(self.navigation_toolbar)
        self.navigation_toolbar.create_ui()
        self.addDockWidget(Qt.BottomDockWidgetArea, self.application_status)
        self.__setup_menu_bar()

    @pyqtSlot()
    def on_show_application_status_widget_triggered(self):
        """Shows and hides application status widget."""
        if self.application_status.isVisible():
            self.application_status.setHidden(True)
        else:
            self.application_status.setVisible(True)

    def __setup_menu_bar(self):
        """Setup menu bar."""
        file_menu = self.menu_bar.addMenu('&File')
        view_menu = self.menu_bar.addMenu('&View')

        # File menu
        quit_action = QuitAction(file_menu)
        file_menu.addAction(quit_action)
        quit_action.on_triggered(quit)

        # View menu
        show_application_log_action = ShowApplicationStatusWidgetAction(view_menu)
        show_application_log_action.on_triggered(self.on_show_application_status_widget_triggered)
        view_menu.addAction(show_application_log_action)
