from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QDockWidget

from pyside6helpers.logger.widget import LoggerWidget
from pyside6helpers.logger.string_io_capture import StringIOCapture


def dock_logger_to_main_window(main_window: QMainWindow, string_io_capture: StringIOCapture=None):
    logger_widget = LoggerWidget(string_io_capture=string_io_capture)

    logger_dock_widget = QDockWidget()
    logger_dock_widget.setWindowTitle("Logger")
    logger_dock_widget.setFeatures(QDockWidget.DockWidgetFeature.NoDockWidgetFeatures)
    logger_dock_widget.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea)
    logger_dock_widget.setWidget(logger_widget)

    main_window.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, logger_dock_widget)
