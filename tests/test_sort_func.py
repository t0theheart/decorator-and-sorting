import unittest
from decorator_and_sorting.decorators import SelectionSortDecorator, InsertionSortDecorator, BubbleSortDecorator


class TestSortFuncs(unittest.TestCase):

    def test_selection_sort(self):
        array = [5, 7, 1, 1, 1, 8, 3, 3, 2, 6, 9, 4]
        sorted_array = [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
        SelectionSortDecorator.sort(array)
        self.assertEqual(array, sorted_array)

    def test_insertion_sort(self):
        array = [5, 7, 1, 1, 1, 8, 3, 3, 2, 6, 9, 4]
        sorted_array = [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
        InsertionSortDecorator.sort(array)
        self.assertEqual(array, sorted_array)

    def test_bubble_sort(self):
        array = [5, 7, 1, 1, 1, 8, 3, 3, 2, 6, 9, 4]
        sorted_array = [1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9]
        BubbleSortDecorator.sort(array)
        self.assertEqual(array, sorted_array)
