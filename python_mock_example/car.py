from abc import abstractmethod
from typing import Protocol


class Car(Protocol):
    @abstractmethod
    def lock(self):
        """Locks the car"""
        ...

    @abstractmethod
    def unlock(self):
        """Unlocks the car"""
        ...
