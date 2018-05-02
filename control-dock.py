# import docker as docker
#
# client = docker.from_env()
# containers = client.containers.list(True)
#
# for container in containers:
#     print(container.attrs['Created'])

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea

from Core.Icon import Icon
from Core.Toolbar import Toolbar

app = QApplication(sys.argv)
main_win = QMainWindow()
toolbar = Toolbar()
toolbar.create_ui()
mdi = QMdiArea()
main_win.addToolBar(toolbar)
main_win.setCentralWidget(mdi)
main_win.setWindowIcon(Icon())
main_win.setWindowTitle('Control dock 0.1.0')
main_win.showMaximized()

if __name__ == '__main__':
    sys.exit(app.exec_())
