from PySide6.QtCore import Qt, QDate, QTime, QDateTime
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLabel, QPushButton, QToolBar, QComboBox,
    QCheckBox, QGroupBox, QSlider, QVBoxLayout, QWidget, QTableWidget,
    QTableWidgetItem, QLineEdit, QProgressBar, QMenu, QStatusBar,
    QTabWidget, QFrame, QScrollArea, QSpinBox, QHBoxLayout, QMainWindow,
    QRadioButton, QDoubleSpinBox, QDateEdit, QTimeEdit, QDateTimeEdit,
    QListWidget, QTreeWidget, QTreeWidgetItem, QTextEdit, QPlainTextEdit,
    QDial, QLCDNumber, QToolButton, QGridLayout, QSplitter
)

from pyside6helpers import icons


class PreviewWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PySide6 Common Widgets Demo")

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Create a toolbar
        self.create_toolbar()

        # Adding QTabWidget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Widget groups in tabs
        self.tab_widget.addTab(self.create_buttons_group(), "Buttons")
        self.tab_widget.addTab(self.create_input_group(), "Inputs")
        self.tab_widget.addTab(self.create_containers_group(), "Containers")
        self.tab_widget.addTab(self.create_views_group(), "Views")
        self.tab_widget.addTab(self.create_display_group(), "Display")

        # Create a status bar
        self.create_status_bar()

        # Create a menu bar
        self.create_menu_bar()

        # Set tooltip for all widgets to their class name
        for widget in self.findChildren(QWidget):
            widget.setToolTip(widget.__class__.__name__)

    def create_toolbar(self):
        self.toolbar = QToolBar("Main Toolbar", self)
        self.addToolBar(self.toolbar)

        actions = [
            ("Home", icons.home(), True),
            ("Settings", icons.settings(), False),
            ("User", icons.user(), False),
        ]

        for text, icon, checkable in actions:
            action = QAction(icon, text, self)
            action.setCheckable(checkable)
            self.toolbar.addAction(action)

        self.toolbar.addSeparator()
        self.toolbar.addWidget(QLabel(" Search: "))
        self.toolbar.addWidget(QLineEdit())

    def create_buttons_group(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Push Buttons
        group1 = QGroupBox("Push Buttons")
        layout1 = QHBoxLayout(group1)
        layout1.addWidget(QPushButton("Normal Button"))
        btn_accent = QPushButton("Accent 1 Button")
        btn_accent.setProperty("accent", "1")
        layout1.addWidget(btn_accent)
        btn_icon = QPushButton("Icon Button")
        btn_icon.setIcon(icons.check())
        layout1.addWidget(btn_icon)
        btn_checkable = QPushButton("Checkable")
        btn_checkable.setCheckable(True)
        btn_checkable.setChecked(True)
        layout1.addWidget(btn_checkable)
        btn_flat = QPushButton("Flat Button")
        btn_flat.setFlat(True)
        layout1.addWidget(btn_flat)
        layout.addWidget(group1)

        # Radio Buttons
        group2 = QGroupBox("Radio Buttons")
        layout2 = QVBoxLayout(group2)
        layout2.addWidget(QRadioButton("Option A"))
        rb = QRadioButton("Option B")
        rb.setChecked(True)
        layout2.addWidget(rb)
        layout2.addWidget(QRadioButton("Option C"))
        layout.addWidget(group2)

        # Check Boxes
        group3 = QGroupBox("Check Boxes")
        layout3 = QVBoxLayout(group3)
        layout3.addWidget(QCheckBox("Enabled"))
        cb = QCheckBox("Checked")
        cb.setChecked(True)
        layout3.addWidget(cb)
        cb3 = QCheckBox("Tristate")
        cb3.setTristate(True)
        cb3.setCheckState(Qt.PartiallyChecked)
        layout3.addWidget(cb3)
        layout.addWidget(group3)

        # Tool Buttons
        group4 = QGroupBox("Tool Buttons")
        layout4 = QHBoxLayout(group4)
        tb1 = QToolButton()
        tb1.setIcon(icons.plus())
        layout4.addWidget(tb1)
        tb2 = QToolButton()
        tb2.setIcon(icons.minus())
        tb2.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        tb2.setText("Decrease")
        layout4.addWidget(tb2)
        layout.addWidget(group4)

        layout.addStretch()
        return widget

    def create_input_group(self):
        widget = QScrollArea()
        widget.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)

        # Text Inputs
        group1 = QGroupBox("Text Inputs")
        layout1 = QGridLayout(group1)
        layout1.addWidget(QLabel("Line Edit:"), 0, 0)
        layout1.addWidget(QLineEdit("Hello World"), 0, 1)
        layout1.addWidget(QLabel("Password:"), 1, 0)
        le_pw = QLineEdit()
        le_pw.setEchoMode(QLineEdit.Password)
        le_pw.setText("password")
        layout1.addWidget(le_pw, 1, 1)
        layout1.addWidget(QLabel("Text Edit:"), 2, 0)
        layout1.addWidget(QTextEdit("Multi-line\nText Edit"), 2, 1)
        layout1.addWidget(QLabel("Plain Text:"), 3, 0)
        layout1.addWidget(QPlainTextEdit("Plain Text Edit"), 3, 1)
        layout.addWidget(group1)

        # Number Inputs
        group2 = QGroupBox("Number Inputs")
        layout2 = QGridLayout(group2)
        layout2.addWidget(QLabel("Spin Box:"), 0, 0)
        layout2.addWidget(QSpinBox(), 0, 1)
        layout2.addWidget(QLabel("Double Spin:"), 1, 0)
        layout2.addWidget(QDoubleSpinBox(), 1, 1)
        layout2.addWidget(QLabel("Dial:"), 2, 0)
        layout2.addWidget(QDial(), 2, 1)
        layout.addWidget(group2)

        # Date/Time Inputs
        group3 = QGroupBox("Date/Time Inputs")
        layout3 = QGridLayout(group3)
        layout3.addWidget(QLabel("Date:"), 0, 0)
        layout3.addWidget(QDateEdit(QDate.currentDate()), 0, 1)
        layout3.addWidget(QLabel("Time:"), 1, 0)
        layout3.addWidget(QTimeEdit(QTime.currentTime()), 1, 1)
        layout3.addWidget(QLabel("DateTime:"), 2, 0)
        layout3.addWidget(QDateTimeEdit(QDateTime.currentDateTime()), 2, 1)
        layout.addWidget(group3)

        # Selection
        group4 = QGroupBox("Selection")
        layout4 = QVBoxLayout(group4)
        combo = QComboBox()
        combo.addItems(["Item 1", "Item 2", "Item 3"])
        layout4.addWidget(combo)
        combo_editable = QComboBox()
        combo_editable.setEditable(True)
        combo_editable.addItems(["Edit 1", "Edit 2"])
        layout4.addWidget(combo_editable)
        layout.addWidget(group4)

        layout.addStretch()
        widget.setWidget(content)
        return widget

    def create_containers_group(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Tab Widget (Nested)
        nested_tabs = QTabWidget()
        nested_tabs.addTab(QLabel("Content of Tab 1"), "Tab 1")
        nested_tabs.addTab(QLabel("Content of Tab 2"), "Tab 2")
        layout.addWidget(nested_tabs)

        # Group Box
        group = QGroupBox("Checkable GroupBox")
        group.setCheckable(True)
        group_layout = QVBoxLayout(group)
        group_layout.addWidget(QPushButton("Inside GroupBox"))
        layout.addWidget(group)

        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(QFrame())
        splitter.addWidget(QFrame())
        # Set frame styles to make them visible
        for i in range(splitter.count()):
            splitter.widget(i).setFrameStyle(QFrame.Box | QFrame.Sunken)
            splitter.widget(i).setLayout(QVBoxLayout())
            splitter.widget(i).layout().addWidget(QLabel(f"Splitter Pane {i+1}"))
        layout.addWidget(splitter)

        layout.addStretch()
        return widget

    def create_views_group(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Table
        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["A", "B", "C"])
        for r in range(3):
            for c in range(3):
                table.setItem(r, c, QTableWidgetItem(f"R{r}C{c}"))
        layout.addWidget(table)

        # List
        list_widget = QListWidget()
        list_widget.addItems(["Item Alpha", "Item Beta", "Item Gamma", "Item Delta"])
        layout.addWidget(list_widget)

        # Tree
        tree = QTreeWidget()
        tree.setHeaderLabels(["Key", "Value"])
        root = QTreeWidgetItem(tree, ["Root", ""])
        child1 = QTreeWidgetItem(root, ["Child 1", "Val 1"])
        child2 = QTreeWidgetItem(root, ["Child 2", "Val 2"])
        root.setExpanded(True)
        layout.addWidget(tree)

        return widget

    def create_display_group(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        # Labels
        layout.addWidget(QLabel("<h1>Heading 1</h1>"))
        layout.addWidget(QLabel("This is a <b>formatted</b> label with <font color='red'>color</font>."))

        # Progress Bar
        pb = QProgressBar()
        pb.setValue(75)
        layout.addWidget(pb)

        pb_inf = QProgressBar()
        pb_inf.setRange(0, 0)
        layout.addWidget(pb_inf)

        # Sliders
        group_sliders = QGroupBox("Sliders")
        slider_layout = QHBoxLayout(group_sliders)
        s_hor = QSlider(Qt.Horizontal)
        s_hor.setValue(50)
        slider_layout.addWidget(s_hor)
        s_ver = QSlider(Qt.Vertical)
        s_ver.setValue(30)
        slider_layout.addWidget(s_ver)
        layout.addWidget(group_sliders)

        # LCD Number
        lcd = QLCDNumber()
        lcd.display(123.45)
        layout.addWidget(lcd)

        layout.addStretch()
        return widget

    def create_status_bar(self):
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Demo ready")
        perm_label = QLabel("Permanent Widget")
        self.statusBar().addPermanentWidget(perm_label)

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(icons.diskette(), "Save")
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        view_menu = menu_bar.addMenu("&View")
        sub_menu = view_menu.addMenu("Toolbars")
        sub_menu.addAction("Main Toolbar").setCheckable(True)
