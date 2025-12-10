from abc import ABC, abstractmethod

class GuestCommand(ABC):
    @abstractmethod
    def execute(self):
        pass
