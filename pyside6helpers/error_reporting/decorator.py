import functools
import traceback

from ._reporting_window import _ReportingWindow
from PySide6.QtWidgets import QApplication


def error_reported(name, exit_on_error=False):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            try:
                return func(*args, **kwargs)

            except Exception as e:
                if QApplication.instance() is None:
                    QApplication()
                window = _ReportingWindow(name, str(e), traceback.format_exc(), exit_on_error)
                window.show()
                raise

        return wrapper
    return decorator
