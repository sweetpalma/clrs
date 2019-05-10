#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Solution:
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in reversed(range(i, len(arr))):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

# Test:
class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [31, 41, 59, 26, 41, 58]
        exp = [26, 31, 41, 41, 58, 59]
        bubble_sort(arr)
        self.assertSequenceEqual(arr, exp)

# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
