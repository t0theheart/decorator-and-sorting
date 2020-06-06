from abc import ABC, abstractmethod


class ProgramABC(ABC):
    @abstractmethod
    def read(self, read_from: str): pass

    @abstractmethod
    def write(self, write_to: str, sort_by: str): pass
