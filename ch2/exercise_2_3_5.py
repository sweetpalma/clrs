#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest
import math


# Solution:
def binary_search(arr, v, low, high):
    while low <= high:
        mid = math.floor((low + high) / 2)
        if arr[mid] == v:
            return mid
        elif v > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


# Test:
class TestBinarySearch(unittest.TestCase):

    def test_binary_search_for_odd_length(self):
        arr = [1, 2, 3, 5, 8]
        for i in range(len(arr)):
            element = arr[i]
            self.assertEqual(binary_search(arr, element, 0, len(arr) - 1), i)

    def test_binary_search_for_even_length(self):
        arr = [1, 2, 3, 5]
        for i in range(len(arr)):
            element = arr[i]
            self.assertEqual(binary_search(arr, element, 0, len(arr) - 1), i)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
