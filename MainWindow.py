from PyQt5.QtWidgets import QMainWindow

from Icon import Icon


class MainWindow(QMainWindow):
    __icon = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Control Dock v0.1.0")
        self.__icon = Icon()
        self.setWindowIcon(self.__icon)
