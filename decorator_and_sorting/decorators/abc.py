from abc import ABC, abstractmethod
from decorator_and_sorting.program import ProgramABC


class SortDecoratorABC(ABC):
    def __init__(self, program: ProgramABC):
        self._program = program

    def read(self, read_from: str):
        raise NotImplementedError('SortDecoratorABC objects has no "read" implementation')

    @staticmethod
    @abstractmethod
    def sort(array: list): pass
