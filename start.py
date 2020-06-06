from decorator_and_sorting.program import Program
from decorator_and_sorting.decorators import BubbleSortDecorator, SelectionSortDecorator, InsertionSortDecorator
from enum import Enum


class Sorting(Enum):
    bubble = 'bubble'
    selection = 'selection'
    insertion = 'insertion'


def main():
    """
        Example of using

        Sorting program started!
        Sort types: "bubble", "selection", "insertion"
        Enter type sort: bubble
        Enter read from: array.txt
        Enter write to: result.txt
        "Bubble sort" used
        Sorting program end.
    """

    program = Program()

    print('Sorting program started!')
    print(f'Sort types: "{Sorting.bubble.value}", "{Sorting.selection.value}", "{Sorting.insertion.value}"')

    sort_type = input('Enter type sort: ')
    read_from = input('Enter read from: ')
    write_to = input('Enter write to: ')

    program.read(read_from)

    if sort_type == Sorting.bubble.value:
        BubbleSortDecorator(program).write(write_to)
    elif sort_type == Sorting.selection.value:
        SelectionSortDecorator(program).write(write_to)
    elif sort_type == Sorting.insertion.value:
        InsertionSortDecorator(program).write(write_to)
    else:
        print(f'Sorting program does not support "{sort_type}" sorting')
        program.write(write_to)

    print('Sorting program end.')


if __name__ == '__main__':
    main()
