import abc

from PyQt5.QtWidgets import QWizardPage


class AbstractPage(QWizardPage):
    """Abstract class used to create wizard pages.

    Attributes:
        _help_text (str): Help text to display on page."""

    _help_text = ''

    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def create_page(self):
        """Method used to create page UI."""
