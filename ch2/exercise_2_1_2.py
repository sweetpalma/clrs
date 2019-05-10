#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Reference:
def insertion_sort(arr): 
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


# Solution:
def reversed_insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key


# Test:
class TestInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        arr = [31, 41, 59, 26, 41, 58]
        exp = [26, 31, 41, 41, 58, 59]
        insertion_sort(arr)
        self.assertSequenceEqual(arr, exp)

    def test_reversed_insertion_sort(self):
        arr = [31, 41, 59, 26, 41, 58]
        exp = [59, 58, 41, 41, 31, 26]
        reversed_insertion_sort(arr)
        self.assertSequenceEqual(arr, exp)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
