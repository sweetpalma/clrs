#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Solution:
def selection_sort(arr):
    for j in range(0, len(arr) - 1):
        smallest = j
        for i in range(j + 1, len(arr)):
            if (arr[i] < arr[smallest]):
                smallest = i
        arr[j], arr[smallest] = arr[smallest], arr[j]


# Test:
class TestSelectionSort(unittest.TestCase):

    def test_selection_sort(self):
        arr = [31, 41, 59, 26, 41, 58]
        exp = [26, 31, 41, 41, 58, 59]
        selection_sort(arr)
        self.assertSequenceEqual(arr, exp)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
