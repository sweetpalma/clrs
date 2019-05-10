#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Solution:
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return None


# Test:
class TestLinearSearch(unittest.TestCase):

    def test_linear_search_found(self):
        arr = ["paul", "andrew", "dan", "abu"]
        for i in range(len(arr)):
            element = arr[i]
            self.assertEqual(linear_search(arr, element), i)

    def test_linear_search_not_found(self):
        arr = ["paul", "andrew", "dan", "abu"]        
        self.assertEqual(linear_search(arr, "kun"), None)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)