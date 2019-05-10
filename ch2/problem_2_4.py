#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest
import math


# Solution:
def modified_merge_sort(arr, p, r):
    inversions = 0
    if p < r:
        q = math.floor((p + r) / 2)
        inversions = inversions + modified_merge_sort(arr, p, q)
        inversions = inversions + modified_merge_sort(arr, q + 1, r)
        inversions = inversions + modified_merge(arr, p, q, r)
    return inversions


# Solution:
def modified_merge(arr, p, q, r):
    arr_left = arr[p:q+1]
    arr_right = arr[q+1:r+1]
    inversions = 0
    i = j = 0
    for k in range(p, r + 1):
        if  j >= len(arr_right):
            arr[k] = arr_left[i]
            i = i + 1
        elif i >= len(arr_left): 
            arr[k] = arr_right[j]
            j = j + 1
        elif arr_left[i] <= arr_right[j]:
            arr[k] = arr_left[i]
            i = i + 1
        elif arr_left[i] >= arr_right[j]:
            inversions = inversions + (q - p + 1) - i
            arr[k] = arr_right[j]
            j = j + 1
    return inversions


# Test: 
class TestInsertions(unittest.TestCase):

    def test_insertions(self):
        self.assertEqual(5, modified_merge_sort([2, 3, 8, 6, 1], 0, 4))
        self.assertEqual(3, modified_merge_sort([2, 4, 1, 3, 5], 0, 4))


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
