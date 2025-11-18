from functools import cache

from PySide6.QtGui import QIcon, QPixmap, QColor, Qt

from pyside6helpers.resources import make_path


def _make_color(filepath, color: QColor):
    pixmap = QPixmap(filepath)
    mask = pixmap.mask()
    white_pixmap = QPixmap(pixmap.size())
    white_pixmap.fill(color)
    white_pixmap.setMask(mask)
    return white_pixmap


@cache
def align_center(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/align-center.png"), color))


@cache
def align_right(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/align-right.png"), color))


@cache
def back(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/back.png"), color))


@cache
def bar_chart(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/bar-chart.png"), color))


@cache
def barcode(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/barcode.png"), color))


@cache
def book(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/book.png"), color))


@cache
def bookmark(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/bookmark.png"), color))


@cache
def briefcase(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/briefcase.png"), color))


@cache
def calendar(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/calendar.png"), color))


@cache
def cancel(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/cancel.png"), color))


@cache
def cells(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/cells.png"), color))


@cache
def certificate(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/certificate.png"), color))


@cache
def chat(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/chat.png"), color))


@cache
def check(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/check.png"), color))


@cache
def clock(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/clock.png"), color))


@cache
def cloud_computing(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/cloud-computing.png"), color))


@cache
def credit_card(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/credit-card.png"), color))


@cache
def csv_file(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/csv-file.png"), color))


@cache
def dashboard(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/dashboard.png"), color))


@cache
def disabled(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/disabled.png"), color))


@cache
def diskette(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/diskette.png"), color))


@cache
def dislike(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/dislike.png"), color))


@cache
def down_arrow(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/down-arrow.png"), color))


@cache
def download(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/download.png"), color))


@cache
def earth_grid(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/earth-grid.png"), color))


@cache
def eject(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/eject.png"), color))


@cache
def email(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/email.png"), color))


@cache
def equalizer(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/equalizer.png"), color))


@cache
def error(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/error.png"), color))


@cache
def exclamation(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/exclamation.png"), color))


@cache
def file(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/file.png"), color))


@cache
def filter(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/filter.png"), color))


@cache
def flag(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/flag.png"), color))


@cache
def flash(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/flash.png"), color))


@cache
def folder(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/folder.png"), color))


@cache
def headphone(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/headphone.png"), color))


@cache
def heart(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/heart.png"), color))


@cache
def home(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/home.png"), color))


@cache
def image(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/image.png"), color))


@cache
def inbox(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/inbox.png"), color))


@cache
def information(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/information.png"), color))


@cache
def justify(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/justify.png"), color))


@cache
def laptop(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/laptop.png"), color))


@cache
def left_align(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/left-align.png"), color))


@cache
def left_arrow(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/left-arrow.png"), color))


@cache
def levels(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/levels.png"), color))


@cache
def lightbulb(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/lightbulb.png"), color))


@cache
def like(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/like.png"), color))


@cache
def link(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/link.png"), color))


@cache
def list(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/list.png"), color))


@cache
def login(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/login.png"), color))


@cache
def logout(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/logout.png"), color))


@cache
def menu(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/menu.png"), color))


@cache
def minus(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/minus.png"), color))


@cache
def more(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/more.png"), color))


@cache
def move(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/move.png"), color))


@cache
def mute(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/mute.png"), color))


@cache
def next(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/next.png"), color))


@cache
def notification(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/notification.png"), color))


@cache
def padlock(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/padlock.png"), color))


@cache
def pause(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/pause.png"), color))


@cache
def pencil(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/pencil.png"), color))


@cache
def photo_camera(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/photo-camera.png"), color))


@cache
def placeholder(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/placeholder.png"), color))


@cache
def play_button(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/play-button.png"), color))


@cache
def plus(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/plus.png"), color))


@cache
def power_button(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/power-button.png"), color))


@cache
def print(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/print.png"), color))


@cache
def push_pin(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/push-pin.png"), color))


@cache
def qr_code(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/qr-code.png"), color))


@cache
def question_bubble(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/question-bubble.png"), color))


@cache
def question(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/question.png"), color))


@cache
def refresh(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/refresh.png"), color))


@cache
def resize(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/resize.png"), color))


@cache
def right_arrow(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/right-arrow.png"), color))


@cache
def screenshot(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/screenshot.png"), color))


@cache
def search(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/search.png"), color))


@cache
def settings(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/settings.png"), color))


@cache
def share(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/share.png"), color))


@cache
def shield(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/shield.png"), color))


@cache
def shopping_cart(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/shopping-cart.png"), color))


@cache
def shuffle(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/shuffle.png"), color))


@cache
def smartphone(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/smartphone.png"), color))


@cache
def star(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/star.png"), color))


@cache
def stop(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/stop.png"), color))


@cache
def tablet(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/tablet.png"), color))


@cache
def tag(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/tag.png"), color))


@cache
def tasks(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/tasks.png"), color))


@cache
def telephone(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/telephone.png"), color))


@cache
def trash(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/trash.png"), color))


@cache
def unlock(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/unlock.png"), color))


@cache
def up_arrow(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/up-arrow.png"), color))


@cache
def upload(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/upload.png"), color))


@cache
def user(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/user.png"), color))


@cache
def video_camera(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/video-camera.png"), color))


@cache
def vision_stroked(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/vision-stroked.png"), color))


@cache
def vision(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/vision.png"), color))


@cache
def volume(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/volume.png"), color))


@cache
def warning(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/warning.png"), color))


@cache
def wifi(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/wifi.png"), color))


@cache
def zoom_in(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/zoom-in.png"), color))


@cache
def zoom_out(color: QColor = Qt.white) -> QIcon:
    return QIcon(_make_color(make_path("icons/zoom-out.png"), color))
