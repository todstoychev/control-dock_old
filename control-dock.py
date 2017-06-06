import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow

app = QApplication(sys.argv)

if __name__ == '__main__':
    main_win = MainWindow()
    main_win.showMaximized()
    sys.exit(app.exec_())
