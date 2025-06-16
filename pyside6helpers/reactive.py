from dataclasses import dataclass, field
from typing import Callable

from PySide6.QtCore import QObject, Slot

from pyside6helpers.python_extensions.singleton_metaclass import SingletonMetaclass


class _QObjectSingletonMetaclass(type(QObject), SingletonMetaclass):
    """Combined metaclass that supports both QObject and Singleton behavior"""
    pass


# TODO : study use case for Observer deletion


@dataclass
class LatestCall:
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)


@dataclass
class Observer:
    channel:  str
    callback: Callable


class Reactive(QObject, metaclass=_QObjectSingletonMetaclass):

    def __init__(self, parent=None):
        super().__init__(parent)
        self._observers: dict[str, list[Observer]] = dict()
        self._latest_calls: dict[str, LatestCall] = dict()

    def add_observer(self, observer: Observer):
        if observer.channel not in self._observers:
            self._observers[observer.channel] = list()

        self._observers[observer.channel].append(observer)

        latest_call = self._latest_calls.get(observer.channel, None)
        if latest_call is not None:
            observer.callback(*latest_call.args, **latest_call.kwargs)

    def remove_observer(self, observer: Observer):
        if observer.channel not in self._observers:
            return

        self._observers[observer.channel].remove(observer)
        if not self._observers[observer.channel]:
            del self._observers[observer.channel]

    @Slot(str, tuple, dict)
    def notify_observers(self, name, *args, **kwargs):
        self._latest_calls[name] = LatestCall(args, kwargs)

        if name not in self._observers:
            return

        for observer in self._observers[name]:
            observer.callback(*args, **kwargs)
