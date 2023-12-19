import datetime
from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, name: str, data: bytes):
        self._name = name
        self._data = data
        self._dateCreated = datetime.datetime.now()
        self._dateModified = datetime.datetime.now()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def setName(self, value: str):
        self._name = value
        self._dateModified = datetime.datetime.now()

    @abstractmethod
    def readData(self):  # add datatype
        pass
