import re
import subprocess

from PyQt5.QtWidgets import QGridLayout, QLabel, QListWidget, QAbstractItemView

from ControlDock.ContainerWizard.Pages.AbstractPage import AbstractPage


class LinkContainers(AbstractPage):
    """
    Link containers page.
    
    Attributes:
        __layout (QGridLayout): Layout.
        __available_container_label (QLabel): Field label.
        __available_containers (list): Available container names.
        available_containers_dropdown (QListWidget): Available containers field.
    """

    __layout = None
    __available_container_label = None
    __available_containers = []
    available_containers_dropdown = None

    def __init__(self):
        super().__init__()
        self.__layout = QGridLayout()
        self.__available_container_label = QLabel('Available containers')
        self.__available_containers = self.__list_available_container_names()
        self.available_containers_dropdown = QListWidget()

    def create_page(self):
        self.setTitle('Link containers')
        self.setSubTitle('Link to other containers.')
        self.setObjectName('link_containers')
        self.setLayout(self.__layout)
        self.available_containers_dropdown.addItems(self.__available_containers)
        self.available_containers_dropdown.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.__layout.addWidget(self.__available_container_label, 0, 0)
        self.__layout.addWidget(self.available_containers_dropdown, 0, 1)

    @staticmethod
    def __list_available_container_names():
        containers = []
        command = subprocess.Popen(['docker ps'], stdout=subprocess.PIPE, shell=True)
        (out, err) = command.communicate()
        rows = out.splitlines()

        for i in range(0, rows.__len__()):
            row = rows[i].__str__()
            row = re.sub(r"^b\'", '', row)
            row = re.sub(r"\'$", '', row)
            row = re.split(r'\s{2,}', row)

            if i == 0:
                continue

            containers.append(row[-1])

        return containers

