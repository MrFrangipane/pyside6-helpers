from PySide6.QtWidgets import QWidget, QGridLayout


def wrap(widget: QWidget):
    """
    Wraps given widget in a widget with a QGridLayout
    """
    central_widget = QWidget()
    central_layout = QGridLayout(central_widget)
    central_layout.addWidget(widget)
    return central_widget
