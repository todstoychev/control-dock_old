from PyQt5.QtWidgets import QLabel, QVBoxLayout

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class Result(AbstractPage):
    """Creates result page.

    Attributes:
        __layout (QVBoxLayout): Layout."""

    __layout = None

    def __init__(self):
        super().__init__()

        self.__layout = QVBoxLayout()
        self.setObjectName('result_page')
        self.setFinalPage(True)

    def create_page(self, container_id=''):
        """Creates page.

        Keyword arguments:
            :argument container_id: Container id."""

        self.setLayout(self.__layout)

        if len(container_id) > 0:
            self.setTitle('Success')
            self.__layout.addWidget(QLabel('Container with ID: \n' + container_id + "  created successfully!"))

            return

        self.setTitle('Error')
        self.__layout.addWidget(QLabel('Something went wrong! Please check your command and try again.'))
