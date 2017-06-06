import os

from PyQt5.QtGui import QIcon


class Icon(QIcon):
    """
    Main window icon.
    """

    def __init__(self, *__args):
        super().__init__(*__args)
        self.addFile(os.path.realpath(__file__ + "/../resources/icons/16x16/docker.png"))
