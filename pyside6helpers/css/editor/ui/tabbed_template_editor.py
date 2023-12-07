"""
TODO : This was directly copied from CSSEditor, rewrite it
"""
import re

from PySide6.QtGui import QFont
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QTabWidget, QPlainTextEdit

from .template_highlighter import TemplateHighlighter


RE_TABS = re.compile(r'^\/\*([^\/\*]+)\*\/$', re.MULTILINE)
DEFAULT_TAB = "CSS"


class TabbedTemplateEditor(QTabWidget):
    changed = Signal()

    def __init__(self, parent=None):
        QTabWidget.__init__(self, parent)

        self.sections = dict()

        self._font = QFont('monospace')
        self._widgets_indexes = dict()

        self.new_tab(DEFAULT_TAB, '')

    def clear(self):
        QTabWidget.clear(self)
        self.sections = dict()
        self._widgets_indexes = dict()

    def new_tab(self, title, text):
        new_editor = QPlainTextEdit()
        new_editor.setFont(self._font)
        new_editor.setPlainText(text)
        TemplateHighlighter(new_editor.document())

        new_editor.textChanged.connect(self._text_changed)
        self._widgets_indexes[new_editor] = self.count()
        self.addTab(new_editor, title)

    def set_plain_text(self, text):
        items = iter(RE_TABS.split(text))
        sections = dict()
        for item in items:
            if not item:
                continue

            tab_name = item.strip()
            tab_text = next(items).strip()

            sections[tab_name] = tab_text

        self.set_sections(sections)

    def set_sections(self, sections):
        self.clear()

        if not sections:
            self.new_tab(DEFAULT_TAB, '')
            return

        self.sections = sections

        for tab_name, tab_text in sections.items():
            self.new_tab(tab_name, tab_text)

    def plain_text(self):
        texts = list()
        for name, text in self.sections.items():
            if not text:
                continue

            texts.append('/* {} */'.format(name))
            texts.append(text)
            texts.append("")

        return '\n'.join(texts)

    def _text_changed(self, *args):
        text_edit = self.sender()
        text = text_edit.toPlainText()
        tab_name = self.tabBar().tabText(self._widgets_indexes[self.sender()])

        self.sections[tab_name] = text

        found = RE_TABS.findall(text)
        if found:
            whole_text = self.plain_text()
            self.set_plain_text(whole_text)

        self.changed.emit()
