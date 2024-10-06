from functools import cache

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from pyside6helpers.resources import make_path


def _make_white(filepath):
    pixmap = QPixmap(filepath)
    mask = pixmap.mask()
    white_pixmap = QPixmap(pixmap.size())
    white_pixmap.fill(Qt.white)
    white_pixmap.setMask(mask)
    return white_pixmap


@cache
def align_center() -> QIcon:
    return QIcon(_make_white(make_path("icons/align-center.png")))


@cache
def align_right() -> QIcon:
    return QIcon(_make_white(make_path("icons/align-right.png")))


@cache
def back() -> QIcon:
    return QIcon(_make_white(make_path("icons/back.png")))


@cache
def bar_chart() -> QIcon:
    return QIcon(_make_white(make_path("icons/bar-chart.png")))


@cache
def barcode() -> QIcon:
    return QIcon(_make_white(make_path("icons/barcode.png")))


@cache
def book() -> QIcon:
    return QIcon(_make_white(make_path("icons/book.png")))


@cache
def bookmark() -> QIcon:
    return QIcon(_make_white(make_path("icons/bookmark.png")))


@cache
def briefcase() -> QIcon:
    return QIcon(_make_white(make_path("icons/briefcase.png")))


@cache
def calendar() -> QIcon:
    return QIcon(_make_white(make_path("icons/calendar.png")))


@cache
def cancel() -> QIcon:
    return QIcon(_make_white(make_path("icons/cancel.png")))


@cache
def certificate() -> QIcon:
    return QIcon(_make_white(make_path("icons/certificate.png")))


@cache
def chat() -> QIcon:
    return QIcon(_make_white(make_path("icons/chat.png")))


@cache
def check() -> QIcon:
    return QIcon(_make_white(make_path("icons/check.png")))


@cache
def clock() -> QIcon:
    return QIcon(_make_white(make_path("icons/clock.png")))


@cache
def cloud_computing() -> QIcon:
    return QIcon(_make_white(make_path("icons/cloud-computing.png")))


@cache
def credit_card() -> QIcon:
    return QIcon(_make_white(make_path("icons/credit-card.png")))


@cache
def dashboard() -> QIcon:
    return QIcon(_make_white(make_path("icons/dashboard.png")))


@cache
def disabled() -> QIcon:
    return QIcon(_make_white(make_path("icons/disabled.png")))


@cache
def diskette() -> QIcon:
    return QIcon(_make_white(make_path("icons/diskette.png")))


@cache
def dislike() -> QIcon:
    return QIcon(_make_white(make_path("icons/dislike.png")))


@cache
def down_arrow() -> QIcon:
    return QIcon(_make_white(make_path("icons/down-arrow.png")))


@cache
def download() -> QIcon:
    return QIcon(_make_white(make_path("icons/download.png")))


@cache
def earth_grid() -> QIcon:
    return QIcon(_make_white(make_path("icons/earth-grid.png")))


@cache
def eject() -> QIcon:
    return QIcon(_make_white(make_path("icons/eject.png")))


@cache
def email() -> QIcon:
    return QIcon(_make_white(make_path("icons/email.png")))


@cache
def equalizer() -> QIcon:
    return QIcon(_make_white(make_path("icons/equalizer.png")))


@cache
def error() -> QIcon:
    return QIcon(_make_white(make_path("icons/error.png")))


@cache
def exclamation() -> QIcon:
    return QIcon(_make_white(make_path("icons/exclamation.png")))


@cache
def file() -> QIcon:
    return QIcon(_make_white(make_path("icons/file.png")))


@cache
def filter() -> QIcon:
    return QIcon(_make_white(make_path("icons/filter.png")))


@cache
def flag() -> QIcon:
    return QIcon(_make_white(make_path("icons/flag.png")))


@cache
def flash() -> QIcon:
    return QIcon(_make_white(make_path("icons/flash.png")))


@cache
def folder() -> QIcon:
    return QIcon(_make_white(make_path("icons/folder.png")))


@cache
def headphone() -> QIcon:
    return QIcon(_make_white(make_path("icons/headphone.png")))


@cache
def heart() -> QIcon:
    return QIcon(_make_white(make_path("icons/heart.png")))


@cache
def home() -> QIcon:
    return QIcon(_make_white(make_path("icons/home.png")))


@cache
def image() -> QIcon:
    return QIcon(_make_white(make_path("icons/image.png")))


@cache
def inbox() -> QIcon:
    return QIcon(_make_white(make_path("icons/inbox.png")))


@cache
def information() -> QIcon:
    return QIcon(_make_white(make_path("icons/information.png")))


@cache
def justify() -> QIcon:
    return QIcon(_make_white(make_path("icons/justify.png")))


@cache
def laptop() -> QIcon:
    return QIcon(_make_white(make_path("icons/laptop.png")))


@cache
def left_align() -> QIcon:
    return QIcon(_make_white(make_path("icons/left-align.png")))


@cache
def left_arrow() -> QIcon:
    return QIcon(_make_white(make_path("icons/left-arrow.png")))


@cache
def levels() -> QIcon:
    return QIcon(_make_white(make_path("icons/levels.png")))


@cache
def like() -> QIcon:
    return QIcon(_make_white(make_path("icons/like.png")))


@cache
def link() -> QIcon:
    return QIcon(_make_white(make_path("icons/link.png")))


@cache
def list() -> QIcon:
    return QIcon(_make_white(make_path("icons/list.png")))


@cache
def login() -> QIcon:
    return QIcon(_make_white(make_path("icons/login.png")))


@cache
def logout() -> QIcon:
    return QIcon(_make_white(make_path("icons/logout.png")))


@cache
def menu() -> QIcon:
    return QIcon(_make_white(make_path("icons/menu.png")))


@cache
def minus() -> QIcon:
    return QIcon(_make_white(make_path("icons/minus.png")))


@cache
def more() -> QIcon:
    return QIcon(_make_white(make_path("icons/more.png")))


@cache
def move() -> QIcon:
    return QIcon(_make_white(make_path("icons/move.png")))


@cache
def mute() -> QIcon:
    return QIcon(_make_white(make_path("icons/mute.png")))


@cache
def next() -> QIcon:
    return QIcon(_make_white(make_path("icons/next.png")))


@cache
def notification() -> QIcon:
    return QIcon(_make_white(make_path("icons/notification.png")))


@cache
def padlock() -> QIcon:
    return QIcon(_make_white(make_path("icons/padlock.png")))


@cache
def pause() -> QIcon:
    return QIcon(_make_white(make_path("icons/pause.png")))


@cache
def pencil() -> QIcon:
    return QIcon(_make_white(make_path("icons/pencil.png")))


@cache
def photo_camera() -> QIcon:
    return QIcon(_make_white(make_path("icons/photo-camera.png")))


@cache
def placeholder() -> QIcon:
    return QIcon(_make_white(make_path("icons/placeholder.png")))


@cache
def play_button() -> QIcon:
    return QIcon(_make_white(make_path("icons/play-button.png")))


@cache
def plus() -> QIcon:
    return QIcon(_make_white(make_path("icons/plus.png")))


@cache
def power_button() -> QIcon:
    return QIcon(_make_white(make_path("icons/power-button.png")))


@cache
def print() -> QIcon:
    return QIcon(_make_white(make_path("icons/print.png")))


@cache
def push_pin() -> QIcon:
    return QIcon(_make_white(make_path("icons/push-pin.png")))


@cache
def qr_code() -> QIcon:
    return QIcon(_make_white(make_path("icons/qr-code.png")))


@cache
def question_bubble() -> QIcon:
    return QIcon(_make_white(make_path("icons/question-bubble.png")))


@cache
def question() -> QIcon:
    return QIcon(_make_white(make_path("icons/question.png")))


@cache
def refresh() -> QIcon:
    return QIcon(_make_white(make_path("icons/refresh.png")))


@cache
def resize() -> QIcon:
    return QIcon(_make_white(make_path("icons/resize.png")))


@cache
def right_arrow() -> QIcon:
    return QIcon(_make_white(make_path("icons/right-arrow.png")))


@cache
def screenshot() -> QIcon:
    return QIcon(_make_white(make_path("icons/screenshot.png")))


@cache
def search() -> QIcon:
    return QIcon(_make_white(make_path("icons/search.png")))


@cache
def settings() -> QIcon:
    return QIcon(_make_white(make_path("icons/settings.png")))


@cache
def share() -> QIcon:
    return QIcon(_make_white(make_path("icons/share.png")))


@cache
def shield() -> QIcon:
    return QIcon(_make_white(make_path("icons/shield.png")))


@cache
def shopping_cart() -> QIcon:
    return QIcon(_make_white(make_path("icons/shopping-cart.png")))


@cache
def shuffle() -> QIcon:
    return QIcon(_make_white(make_path("icons/shuffle.png")))


@cache
def smartphone() -> QIcon:
    return QIcon(_make_white(make_path("icons/smartphone.png")))


@cache
def star() -> QIcon:
    return QIcon(_make_white(make_path("icons/star.png")))


@cache
def stop() -> QIcon:
    return QIcon(_make_white(make_path("icons/stop.png")))


@cache
def tablet() -> QIcon:
    return QIcon(_make_white(make_path("icons/tablet.png")))


@cache
def tag() -> QIcon:
    return QIcon(_make_white(make_path("icons/tag.png")))


@cache
def tasks() -> QIcon:
    return QIcon(_make_white(make_path("icons/tasks.png")))


@cache
def telephone() -> QIcon:
    return QIcon(_make_white(make_path("icons/telephone.png")))


@cache
def trash() -> QIcon:
    return QIcon(_make_white(make_path("icons/trash.png")))


@cache
def unlock() -> QIcon:
    return QIcon(_make_white(make_path("icons/unlock.png")))


@cache
def up_arrow() -> QIcon:
    return QIcon(_make_white(make_path("icons/up-arrow.png")))


@cache
def upload() -> QIcon:
    return QIcon(_make_white(make_path("icons/upload.png")))


@cache
def user() -> QIcon:
    return QIcon(_make_white(make_path("icons/user.png")))


@cache
def video_camera() -> QIcon:
    return QIcon(_make_white(make_path("icons/video-camera.png")))


@cache
def vision_stroked() -> QIcon:
    return QIcon(_make_white(make_path("icons/vision-stroked.png")))


@cache
def vision() -> QIcon:
    return QIcon(_make_white(make_path("icons/vision.png")))


@cache
def volume() -> QIcon:
    return QIcon(_make_white(make_path("icons/volume.png")))


@cache
def warning() -> QIcon:
    return QIcon(_make_white(make_path("icons/warning.png")))


@cache
def wifi() -> QIcon:
    return QIcon(_make_white(make_path("icons/wifi.png")))


@cache
def zoom_in() -> QIcon:
    return QIcon(_make_white(make_path("icons/zoom-in.png")))


@cache
def zoom_out() -> QIcon:
    return QIcon(_make_white(make_path("icons/zoom-out.png")))
