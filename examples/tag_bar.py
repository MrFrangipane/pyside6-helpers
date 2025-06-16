from PySide6.QtWidgets import QGridLayout, QApplication, QWidget, QLabel

from pyside6helpers.tag_bar import TagBar
from pyside6helpers import css


class Window(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.one = TagBar()
        self.one.autocompletables = ['Layout', 'Buildings', 'Characters', 'Animation']
        self.one.tag_created.connect(lambda tag: print(f"Tag '{tag}' created"))
        self.two = TagBar()

        layout = QGridLayout(self)
        layout.addWidget(QLabel("TagBar 1 :"), 0, 0)
        layout.addWidget(self.one, 0, 1)
        layout.addWidget(QLabel("TagBar 2 :"), 1, 0)
        layout.addWidget(self.two, 1, 1)
        layout.addWidget(QWidget(), 2, 0)
        layout.setColumnStretch(1, 100)
        layout.setRowStretch(2, 100)

        self.one.set_tags(['Modeling', 'Vegetation', 'Scatterable', 'Animation'])
        self.two.set_tags(['Flowers'])


if __name__ == '__main__':
    app = QApplication([])
    css.load_onto(app)

    window = Window()
    window.resize(800, 150)
    window.show()

    app.exec()
