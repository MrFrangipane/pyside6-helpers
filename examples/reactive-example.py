from PySide6.QtCore import QObject, Signal, Slot, QThread
from PySide6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton

from pyside6helpers.reactive import Observer, Reactive


class Worker(QObject):
    progress_updated = Signal(int)
    work_finished = Signal(str)
    error_occurred = Signal(str)

    def __init__(self):
        super().__init__()
        self.should_stop = False

    @Slot()
    def do_work(self):
        try:
            for i in range(11):  # 0 to 10
                if self.should_stop:
                    break

                QThread.currentThread().sleep(2)
                self.progress_updated.emit(i * 10)

            if not self.should_stop:
                self.work_finished.emit("Worker finished successfully!")

        except Exception as e:
            self.error_occurred.emit(str(e))

    @Slot()
    def stop_work(self):
        self.should_stop = True


class ReactiveWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.label = QLabel()
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        Reactive().add_observer(Observer(
            channel="DemoChannel",
            callback=lambda new_text: self.label.setText(new_text)
        ))

        self.resize(300, 150)


class EmitterWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.lineedit = QLineEdit()
        self.lineedit.textChanged.connect(lambda new_text: Reactive().notify_observers("DemoChannel", new_text))

        self.button = QPushButton("Send")
        self.button.clicked.connect(self._button_clicked)

        layout = QVBoxLayout(self)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button)

        self.worker: Worker | None = None
        self.thread: QThread | None = None

        self.start_worker()

    @staticmethod
    def _button_clicked():
        Reactive().notify_observers("DemoChannel", "The button was clicked")

    def start_worker(self):
        if self.thread is None or not self.thread.isRunning():
            self.thread = QThread()
            self.worker = Worker()

            self.worker.moveToThread(self.thread)

            self.thread.started.connect(self.worker.do_work)
            self.worker.progress_updated.connect(lambda progress: Reactive().notify_observers("DemoChannel", f"Progress: {progress}"))
            self.worker.work_finished.connect(self.thread.quit)
            self.worker.error_occurred.connect(self.thread.quit)
            self.thread.finished.connect(self.on_worker_finished)

            self.thread.start()

    def on_worker_finished(self):
        if self.worker:
            self.worker.deleteLater()
            self.worker = None
        if self.thread:
            self.thread.deleteLater()
            self.thread = None

    @Slot()
    def  stop_worker(self):
        if self.worker:
            self.worker.stop_work()
        if self.thread and self.thread.isRunning():
            self.thread.quit()
            self.thread.wait(3000)


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName('Reactive Demo')

    Reactive().notify_observers(
        "DemoChannel",
        "Message before Observer registration, will be discarded by the next one"
    )
    Reactive().notify_observers(
        "DemoChannel",
        "Message before Observer registration"
    )

    reactive_a = ReactiveWidget()
    reactive_a.show()

    reactive_b = ReactiveWidget()
    reactive_b.show()

    emitter_widget = EmitterWidget()
    emitter_widget.show()

    app.aboutToQuit.connect(emitter_widget.stop_worker)

    app.exec()
