from ControlDock.MenuBarActions.MenuBarAction import MenuBarAction


class QuitAction(MenuBarAction):
    """Menu bar quit action."""

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText('&Quit')
        self.setShortcut('Ctrl+Q')
        self.setStatusTip('Quit application.')
        self.setToolTip('Quit application.')

    def on_triggered(self, slot):
        super().on_triggered(slot)
