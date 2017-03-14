from PyQt5.QtWidgets import QCheckBox


class ShowAllCheckbox(QCheckBox):
    """Show all containers check box."""

    def __init__(self, *__args):
        super().__init__(*__args)
        self.setText('Show all containers')
        self.setToolTip('Shows all containers when checked.')
        self.setObjectName('show_all_containers_checkbox')
