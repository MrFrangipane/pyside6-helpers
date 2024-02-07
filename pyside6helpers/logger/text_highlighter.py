import re
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont, QColor, QBrush


color_debug = QBrush(QColor(161, 161, 161))
color_debug_path = QBrush(QColor(138, 138, 138))

color_info_path = QBrush(QColor(179, 179, 179))

color_warning = QBrush(QColor(255, 185, 118))
color_warning_path = QBrush(QColor(186, 136, 115))

color_critical = QBrush(QColor(255, 104, 104))
color_critical_path = QBrush(QColor(191, 111, 111))

color_file = QBrush(QColor(194, 194, 194))
color_line = QBrush(QColor(216, 216, 216))

font_monospaced = QFont("Courier")
# font_monospaced.setStyleHint(QFont.TypeWriter)
font_monospaced.setPointSize(9)
font_monospaced.setWeight(QFont.Bold)

#
# LOG
DEBUG_RE = re.compile(r"^DEBUG:.+")
DEBUG_FORMAT = QTextCharFormat()
DEBUG_FORMAT.setForeground(color_debug)
DEBUG_PATH_RE = re.compile(r"^DEBUG:([^:]+:)")
DEBUG_PATH_FORMAT = QTextCharFormat()
DEBUG_PATH_FORMAT.setForeground(color_debug_path)
DEBUG_PATH_FORMAT.setFontItalic(True)

INFO_RE = re.compile(r"^INFO:.+")
INFO_FORMAT = QTextCharFormat()
INFO_PATH_RE = re.compile(r"^INFO:([^:]+:)")
INFO_PATH_FORMAT = QTextCharFormat()
INFO_PATH_FORMAT.setForeground(color_info_path)
INFO_PATH_FORMAT.setFontItalic(True)

WARNING_RE = re.compile(r"^WARNING:.+")
WARNING_FORMAT = QTextCharFormat()
WARNING_FORMAT.setForeground(color_warning)
WARNING_PATH_RE = re.compile(r"^WARNING:([^:]+:)")
WARNING_PATH_FORMAT = QTextCharFormat()
WARNING_PATH_FORMAT.setForeground(color_warning_path)
WARNING_PATH_FORMAT.setFontItalic(True)

ERROR_RE = re.compile(r"^ERROR:.+")
ERROR_FORMAT = QTextCharFormat()
ERROR_FORMAT.setForeground(color_critical)
ERROR_PATH_RE = re.compile(r"^ERROR:([^:]+:)")
ERROR_PATH_FORMAT = QTextCharFormat()
ERROR_PATH_FORMAT.setForeground(color_critical_path)
ERROR_PATH_FORMAT.setFontItalic(True)

CRITICAL_RE = re.compile(r"^CRITICAL:.+")
CRITICAL_FORMAT = QTextCharFormat()
CRITICAL_FORMAT.setForeground(color_critical)
CRITICAL_PATH_RE = re.compile(r"^CRITICAL:([^:]+:)")
CRITICAL_PATH_FORMAT = QTextCharFormat()
CRITICAL_PATH_FORMAT.setForeground(color_critical_path)
CRITICAL_PATH_FORMAT.setFontItalic(True)

#
# TRACEBACK
LINE_FILE_RE = re.compile(r"^\s\s\S.+")
LINE_FILE_FORMAT = QTextCharFormat()
LINE_FILE_FORMAT.setForeground(color_file)

LINE_CODE_RE = re.compile(r"^\s\s\s\s\S.+")
LINE_CODE_FORMAT = QTextCharFormat()
LINE_CODE_FORMAT.setFont(font_monospaced)

FILE_RE = re.compile(r"\"[^\"]+\"")
FILE_FORMAT = QTextCharFormat()
FILE_FORMAT.setFontItalic(True)

CALL_RE = re.compile(r", in ([^$]+)$")
CALL_FORMAT = QTextCharFormat()
CALL_FORMAT.setFont(font_monospaced)

LINE_RE = re.compile(r"line \d+")
LINE_FORMAT = QTextCharFormat()
LINE_FORMAT.setForeground(color_line)


class TextHighlighter(QSyntaxHighlighter):
    RULES = {
        DEBUG_RE: DEBUG_FORMAT, DEBUG_PATH_RE: DEBUG_PATH_FORMAT,
        INFO_RE: INFO_FORMAT, INFO_PATH_RE: INFO_PATH_FORMAT,
        WARNING_RE: WARNING_FORMAT, WARNING_PATH_RE: WARNING_PATH_FORMAT,
        ERROR_RE: ERROR_FORMAT, ERROR_PATH_RE: ERROR_PATH_FORMAT,
        CRITICAL_RE: CRITICAL_FORMAT, CRITICAL_PATH_RE: CRITICAL_PATH_FORMAT,
        LINE_FILE_RE: LINE_FILE_FORMAT,
        LINE_CODE_RE: LINE_CODE_FORMAT,
        CALL_RE: CALL_FORMAT,
        LINE_RE: LINE_FORMAT
    }

    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

    def highlightBlock(self, text):
        for expression, style in self.RULES.items():
            for match in expression.finditer(text):
                if len(match.regs) > 1:
                    start, end = match.span(1)
                else:
                    start, end = match.span()
                self.setFormat(start, end - start, style)
