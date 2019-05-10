#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest
import math


# Reference:
def merge_sort(arr, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)


# Solution:
def merge(arr, p, q, r):
    arr_left = arr[p:q+1]
    arr_right = arr[q+1:r+1]
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
            arr[k] = arr_right[j]
            j = j + 1


# Test:
class TestMergeSort(unittest.TestCase):

    class MergeCase:
        pass

    def helper_build_case(self, left, right):
        case = TestMergeSort.MergeCase()
        case.arr = left + right
        case.p = 0
        case.q = len(left) - 1
        case.r = len(left) + len(right) - 1
        return case

    def test_merge(self):
        cases = [
            self.helper_build_case([1], [2]),
            self.helper_build_case([2], [1]),
            self.helper_build_case([1], [2, 3, 4, 5]),
            self.helper_build_case([1, 4], [2, 3, 5]),
            self.helper_build_case([1, 4, 5], [2, 3]),
            self.helper_build_case([1, 2, 4, 5], [3]),
        ]
        for case in cases:
            arr = case.arr
            exp = sorted(arr)
            merge(arr, case.p, case.q, case.r)
            self.assertSequenceEqual(arr, exp)

    def test_merge_sort(self):
        arr = [31, 41, 59, 26, 41, 58]
        exp = [26, 31, 41, 41, 58, 59]
        merge_sort(arr, 0, len(arr) - 1)
        self.assertSequenceEqual(arr, exp)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
