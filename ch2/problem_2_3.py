#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Reference:
def horner_rule(arr, x):
    y = 0
    for i in reversed(range(0, len(arr))):
        y = arr[i] + x * y
    return y


# Solution:
def naive_horner_rule(arr, x):
    y = 0
    for k in range(0, len(arr)):
        temp = 1
        for i in range(0, k):
            temp = temp * x
        y = y + arr[k] * temp
    return y


# Test:
class TestHornerRule(unittest.TestCase):

    def test_horner_rule(self):
        arr = [9, 7, 5, 3, 1]
        x_v = 2
        exp = 83
        self.assertEqual(horner_rule(arr, x_v), exp)

    def test_naive_horner_rule(self):
        arr = [9, 7, 5, 3, 1]
        x_v = 2
        exp = 83
        self.assertEqual(naive_horner_rule(arr, x_v), exp)

# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
