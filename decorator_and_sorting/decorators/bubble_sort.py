from decorator_and_sorting.program.abc import ProgramABC


class BubbleSortDecorator(ProgramABC):
    def __init__(self, program: ProgramABC):
        self._program: ProgramABC = program
        self._array: list = []

    @staticmethod
    def sort(array: list):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(array) - 1):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swapped = True

    def write(self, write_to: str, sort_by: str = 'Sorted by "Bubble sort"'):
        print('"Bubble sort" used')
        self._array = self._program._array
        self.sort(self._array)
        self._program.write(write_to, sort_by)

    def read(self, read_from: str):
        raise NotImplementedError('BubbleSortDecorator objects has no "read" implementation')
