from decorator_and_sorting.program.abc import ProgramABC


class SelectionSortDecorator(ProgramABC):
    def __init__(self, program: ProgramABC):
        self._program: ProgramABC = program
        self._array: list = []

    @staticmethod
    def sort(array: list):
        for i in range(len(array)):
            lowest_value_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[lowest_value_index]:
                    lowest_value_index = j
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]

    def write(self, write_to: str, sort_by: str = 'Sorted by "Selection sort"'):
        print('"Selection sort" used')
        self._array = self._program._array
        self.sort(self._array)
        self._program.write(write_to, sort_by)

    def read(self, read_from: str):
        raise NotImplementedError('SelectionSortDecorator objects has no "read" implementation')
