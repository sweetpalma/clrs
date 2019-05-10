#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest
try:
    from .exercise_2_3_5 import binary_search
    from .exercise_2_3_2 import merge_sort
except:
    from exercise_2_3_5 import binary_search
    from exercise_2_3_2 import merge_sort


# Solution:
def pair_search(arr, x):
    merge_sort(arr, 0, len(arr) - 1)
    for y in arr:
        i = binary_search(arr, x - y, 0, len(arr) - 1)
        if i != None:
            return True
    return False


# Test:
class TestPairSearch(unittest.TestCase):

    def test_pair_search(self):
        self.assertTrue (pair_search([1, 2], 3))
        self.assertTrue (pair_search([2, 1], 3))
        self.assertFalse(pair_search([2, 0], 3))
        self.assertTrue (pair_search([2, 10, 15, 1, 3], 3))
        self.assertTrue (pair_search([1, 10, 15, 2, 3], 3))
        self.assertFalse(pair_search([2, 10, 15, 3, 3], 3))


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
    