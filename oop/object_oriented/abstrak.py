from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def belajar(self, pelajaran: str) -> None: pass