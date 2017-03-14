import os

from PyQt5.QtGui import QIcon


class WindowIcon:
    """Creates window icon object used globally in the project."""

    @staticmethod
    def get_icon(path=None):
        """get_icon() -> QIcon

        Returns the QIcon object.

        Keyword arguments:
            path (str): Path to icon file."""
        if path is None:
            path = os.path.dirname(os.path.realpath(__file__))
            path += '/../resources/icons/16x16/icon.png'

        return QIcon(path)
