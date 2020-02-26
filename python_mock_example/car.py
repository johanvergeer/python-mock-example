from abc import abstractmethod
from typing import Protocol


class Car(Protocol):
    @abstractmethod
    def lock(self):
        ...

    @abstractmethod
    def unlock(self):
        ...
