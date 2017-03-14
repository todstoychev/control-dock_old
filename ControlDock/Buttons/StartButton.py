import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QPushButton


class StartButton(QPushButton):
    """Start containers button.

    Attributes:
        :param path (str): Current path"""

    path = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText('Start')
        self.setIcon(QIcon(self.path + '/../../resources/icons/16x16/start.png'))
