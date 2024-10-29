"""
prompt :
a pyside6 qmainwindow with all the common widgets: toolbar with icons, label, pushbutton, checkable pushbutton, combo box, check box, qgroupbox, qslider, qtable, qlabel, qlineedit, qprogressbar, qmenu, qaction, qaction checkable, sub qmenu, status bar with 'frangitron-logo.png', tabwidget, qframe, qscrollarea, qspinbox. each widget group should be in a qgroupbox. separate group creation into methods.
"""
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QPixmap
from PySide6.QtWidgets import (
    QMainWindow, QLabel, QPushButton, QToolBar, QComboBox,
    QCheckBox, QGroupBox, QSlider, QVBoxLayout, QWidget, QTableWidget,
    QTableWidgetItem, QLineEdit, QProgressBar, QMenu, QStatusBar,
    QTabWidget, QFrame, QScrollArea, QSpinBox, QHBoxLayout
)

from pyside6helpers import icons


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PySide6 Widget Example")
        self.setGeometry(100, 100, 1000, 800)

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create a toolbar
        self.create_toolbar()

        # Adding QTabWidget
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        # Widget groups in tabs
        tab_widget.addTab(self.create_label_button_group(), "Labels and Buttons")
        tab_widget.addTab(self.create_combo_check_group(), "ComboBox and CheckBox")
        tab_widget.addTab(self.create_slider_group(), "Slider")
        tab_widget.addTab(self.create_table_group(), "Table")
        tab_widget.addTab(self.create_additional_widgets_group(), "Additional Widgets")

        # Create a status bar
        self.create_status_bar()

        # Create a menu bar
        self.create_menu_bar()

    def create_toolbar(self):

        # Create a checkable QAction
        self.checkable_action = QAction("Checkable Action")
        self.checkable_action.setIcon(icons.levels())
        self.checkable_action.setIconVisibleInMenu(True)
        self.checkable_action.setCheckable(True)

        self.button_action = QAction("Button Action")
        self.button_action.setIcon(icons.wifi())
        self.button_action.setIconVisibleInMenu(True)

        # Create a QToolBar
        self.toolbar = QToolBar("My Toolbar", self)
        self.toolbar.setOrientation(Qt.Horizontal)
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.orientationChanged.connect(self._update_button_style)
        self.addToolBar(self.toolbar)

        # Add the QAction to the toolbar
        self.toolbar.addWidget(QLabel('Test'))
        self.toolbar.addAction(self.checkable_action)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(QLabel('Testouille'))
        self.toolbar.addAction(self.button_action)


    def create_label_button_group(self):
        group_box = QGroupBox("Labels and Buttons")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        label = QLabel("This is a label")
        layout.addWidget(label)

        push_button = QPushButton("Click Me")
        layout.addWidget(push_button)

        checkable_button = QPushButton("Checkable Button")
        checkable_button.setCheckable(True)
        layout.addWidget(checkable_button)

        return group_box

    def create_combo_check_group(self):
        group_box = QGroupBox("ComboBox and CheckBox")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        combo_box = QComboBox()
        combo_box.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo_box)

        check_box = QCheckBox("Check Me")
        layout.addWidget(check_box)

        return group_box

    def create_slider_group(self):
        group_box = QGroupBox("Slider")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        slider = QSlider(Qt.Horizontal)
        layout.addWidget(slider)

        return group_box

    def create_table_group(self):
        group_box = QGroupBox("Table")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        table.setItem(0, 0, QTableWidgetItem("Item 1-1"))
        table.setItem(1, 0, QTableWidgetItem("Item 2-1"))
        table.setItem(2, 0, QTableWidgetItem("Item 3-1"))
        layout.addWidget(table)

        return group_box

    def create_additional_widgets_group(self):
        group_box = QGroupBox("Additional Widgets")
        layout = QVBoxLayout()
        group_box.setLayout(layout)

        label_2 = QLabel("This is another label")
        layout.addWidget(label_2)

        line_edit = QLineEdit()
        layout.addWidget(line_edit)

        progress_bar = QProgressBar()
        progress_bar.setValue(50)
        layout.addWidget(progress_bar)

        spin_box = QSpinBox()
        layout.addWidget(spin_box)

        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        frame.setLineWidth(2)
        frame_layout = QHBoxLayout()
        frame_layout.addWidget(QLabel("Inside frame"))
        frame.setLayout(frame_layout)
        layout.addWidget(frame)

        scroll_area = QScrollArea()
        scroll_area_widget = QWidget()
        scroll_area_layout = QVBoxLayout()
        scroll_area_widget.setLayout(scroll_area_layout)
        for i in range(50):
            scroll_area_layout.addWidget(QLabel(f"Scrollable label {i + 1} " * 15))
        scroll_area.setWidget(scroll_area_widget)
        scroll_area.setWidgetResizable(True)
        layout.addWidget(scroll_area)

        return group_box

    def create_status_bar(self):
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        status_bar.showMessage("Ready")
        logo_label = QLabel()
        logo_label.setPixmap(QPixmap("../resources/frangitron-logo.png"))
        status_bar.addPermanentWidget(logo_label)

    def create_menu_bar(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")
        edit_menu = menu_bar.addMenu("Edit")

        new_action = QAction("New", self)
        open_action = QAction("Open", self)

        file_menu.addAction(new_action)
        file_menu.addAction(open_action)

        sub_menu = QMenu("Sub Menu", self)

        sub_menu.addAction(self.checkable_action)
        sub_menu.addAction(self.button_action)
        edit_menu.addMenu(sub_menu)

    def _update_button_style(self):
        if self.toolbar.orientation() == Qt.Vertical:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        elif self.toolbar.orientation() == Qt.Horizontal:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
