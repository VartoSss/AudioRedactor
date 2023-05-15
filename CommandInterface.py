from abc import ABC, abstractmethod


class CommandInterface(ABC):
    @abstractmethod
    def execute():
        pass

    @abstractmethod
    def undo():
        pass
