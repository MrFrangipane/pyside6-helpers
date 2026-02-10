import sys
from binascii import hexlify

from PySide6.QtWidgets import (
    QApplication,QWidget, QVBoxLayout,
    QListWidget, QTextEdit, QLabel, QSplitter, QFrame
)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QMimeData


from pyside6helpers.main_window import MainWindow
from pyside6helpers import css


class ClipboardInspector(MainWindow):
    def __init__(self):
        super().__init__()

        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Header
        self.status_label = QLabel("Copy something to see its internal MIME data!")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.status_label)

        # Splitter for List and Preview
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # Left Side: Formats List
        self.format_list = QListWidget()
        self.format_list.itemSelectionChanged.connect(self.display_format_content)
        splitter.addWidget(self.format_list)

        # Right Side: Preview Area
        self.preview_container = QWidget()
        preview_layout = QVBoxLayout(self.preview_container)
        
        self.text_preview = QTextEdit()
        self.text_preview.setReadOnly(True)
        
        self.image_preview = QLabel("No Image Data")
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setFrameStyle(QFrame.Shape.StyledPanel)
        
        preview_layout.addWidget(QLabel("Content Preview:"))
        preview_layout.addWidget(self.text_preview)
        preview_layout.addWidget(self.image_preview)
        self.image_preview.hide() # Hidden by default
        
        splitter.addWidget(self.preview_container)
        splitter.setStretchFactor(1, 2)
        
        main_layout.addWidget(splitter)
        main_layout.setStretch(1, 1)

        # Connect to Clipboard changes
        self.clipboard = QApplication.clipboard()
        self.clipboard.dataChanged.connect(self.update_clipboard_info)

        # Initial Load
        self.update_clipboard_info()

    def update_clipboard_info(self):
        """Triggered when the system clipboard content changes."""
        mime_data: QMimeData = self.clipboard.mimeData()
        formats = mime_data.formats() # Returns list of available MIME types [1]

        self.format_list.clear()
        if not formats:
            self.status_label.setText("Clipboard is empty.")
            return

        self.status_label.setText(f"Detected {len(formats)} format(s) in clipboard.")
        for fmt in formats:
            self.format_list.addItem(fmt)

        # Select first item by default
        if self.format_list.count() > 0:
            self.format_list.setCurrentRow(0)

    def display_format_content(self):
        """Displays the content of the selected MIME type."""
        selected_items = self.format_list.selectedItems()
        if not selected_items:
            return

        mime_type = selected_items[0].text()
        mime_data = self.clipboard.mimeData()
        data = mime_data.data(mime_type)

        # Reset views
        self.text_preview.show()
        self.image_preview.hide()
        self.text_preview.clear()

        # Handle specific types for better visualization
        if "image" in mime_type:
            image = QImage.fromData(data)
            if not image.isNull():
                pixmap = QPixmap.fromImage(image)
                scaled_pixmap = pixmap.scaled(
                    self.image_preview.size(), 
                    Qt.AspectRatioMode.KeepAspectRatio, 
                    Qt.TransformationMode.SmoothTransformation
                )
                self.image_preview.setPixmap(scaled_pixmap)
                self.image_preview.show()
                self.text_preview.hide()
            else:
                self.text_preview.setPlainText(f"[Binary Image Data: {len(data)} bytes]")
        
        elif "text/html" in mime_type:
            self.text_preview.setHtml(str(data, encoding="utf-8", errors="replace"))
        
        elif "text" in mime_type or "json" in mime_type or "xml" in mime_type:
            try:
                content = str(data, encoding="utf-8")
            except UnicodeDecodeError:
                content = f"[Binary Data: {len(data)} bytes]"
            self.text_preview.setPlainText(content)
        
        else:
            # Fallback for unknown/binary formats
            hex_view = hexlify(data.toHex().data(), sep=" ").decode(encoding="utf-8")
            self.text_preview.setPlainText(f"Raw Hex Data:\n{hex_view}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Clipboard Inspector")
    app.setOrganizationName("Frangitron")
    css.load_onto(app)

    window = ClipboardInspector()
    window.show()

    sys.exit(app.exec())
