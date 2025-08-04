from abc import ABC, abstractmethod

class User(ABC):

    @abstractmethod
    def role(self, _set_role: str) -> None: pass

    @abstractmethod
    def is_resign(self, resign: bool) -> None: pass

class Staff(User):

    def jobdesk(self, set_jobdesk: str) -> None:
        print(set_jobdesk)

    def role(self, _set_role: str) -> None: print(_set_role)

    def is_resign(self, resign: bool) -> None: print("Kamu dikeluarkan secara suka rela.")
