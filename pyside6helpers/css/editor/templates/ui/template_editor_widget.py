import re
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QTabWidget, QPlainTextEdit, QVBoxLayout, QWidget

from .template_highlighter import TemplateHighlighter

DEFAULT_TAB = "Main"
RE_TABS = re.compile(r'^\/\*#([^\/\*#]+)\*\/$', re.MULTILINE)

class TemplateEditorWidget(QTabWidget):
    changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._font = QFont('monospace')
        self._font.setStyleHint(QFont.Monospace)
        self.sections = {}
        self._editors = {}

    def set_sections(self, sections):
        self.blockSignals(True)
        self.clear()
        self.sections = sections.copy()
        self._editors = {}
        
        if not self.sections:
            self.sections[DEFAULT_TAB] = ""

        for title, text in self.sections.items():
            self._add_tab(title, text)
        self.blockSignals(False)

    def get_sections(self):
        return self.sections

    def _add_tab(self, title, text):
        editor = QPlainTextEdit()
        editor.setFont(self._font)
        editor.setPlainText(text)
        editor.setTabStopDistance(QFontMetrics(self._font).horizontalAdvance(' ') * 4)
        TemplateHighlighter(editor.document())
        editor.textChanged.connect(lambda: self._on_text_changed(title, editor))
        
        self.addTab(editor, title)
        self._editors[title] = editor

    def _on_text_changed(self, title, editor):
        text = editor.toPlainText()
        self.sections[title] = text
        
        # Check if new sections were added via /*# Section */
        if RE_TABS.search(text):
            # This is a bit complex to handle mid-edit without losing focus/cursor
            # For now, let's just emit changed and maybe the parent can handle it if needed
            # or we can implement a "Refresh Tabs" button.
            # Original code did: 
            # found = RE_TABS.findall(text)
            # if found:
            #     whole_text = self.plain_text()
            #     self.set_plain_text(whole_text)
            pass

        self.changed.emit()
