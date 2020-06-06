from decorator_and_sorting.program.abc import ProgramABC
import json


class Program(ProgramABC):
    def __init__(self):
        self._array: list = []

    def read(self, read_from: str):
        with open(read_from, 'r') as f:
            line = f.readline()
            self._array = json.loads(line)

    def write(self, write_to: str, sort_by: str = 'Not sorted'):
        with open(write_to, 'w') as f:
            f.write(f'{self._array}\n')
            f.write(f'{sort_by}')
