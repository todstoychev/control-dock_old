from ControlDock.MenuBarActions.MenuBarAction import MenuBarAction


class ShowApplicationStatusWidgetAction(MenuBarAction):
    """Creates show application status action."""

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText('Show application status')
        self.setStatusTip('Shows application status widget.')
        self.setToolTip('Shows application status widget.')
        self.setCheckable(True)
        self.setChecked(True)

    def on_triggered(self, slot):
        super().on_triggered(slot)
