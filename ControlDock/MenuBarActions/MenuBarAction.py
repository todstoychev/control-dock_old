from abc import abstractmethod

from PyQt5.QtWidgets import QAction


class MenuBarAction(QAction):
    """Abstract class to be extend by all menu actions."""

    def __init__(self, *__args):
        super().__init__(*__args)

    @abstractmethod
    def on_triggered(self, slot):
        """Connects triggered signal to slot.

        Parameters
        ----------
        :param slot: Slot reference."""
        self.triggered.connect(slot)
