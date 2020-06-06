from decorator_and_sorting.decorators.abc import SortDecoratorABC
from decorator_and_sorting.program.abc import ProgramABC


class InsertionSortDecorator(ProgramABC, SortDecoratorABC):
    @staticmethod
    def sort(array: list):
        for i in range(1, len(array)):
            item_to_insert = array[i]
            j = i - 1
            while j >= 0 and array[j] > item_to_insert:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = item_to_insert

    def write(self, write_to: str, sort_by: str = 'Sorted by "Insertion sort"'):
        self.sort(self._program._array)
        self._program.write(write_to, sort_by)

    def read(self, read_from: str):
        super().read(read_from)