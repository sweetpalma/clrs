#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest


# Solution:
def binary_sum(a, b):
    n = len(a)
    c = list()
    carry = 0
    for i in reversed(range(0, n)):
        paired = a[i] + b[i] + carry
        if paired > 1:
            c.insert(0, paired - 2)
            carry = 1
        else:
            c.insert(0, paired)
            carry = 0
    c.insert(0, carry)
    return c


# Test:
class TestBinarySum(unittest.TestCase):

    def helper_int_to_binary(self, n):
        binary_string = '{0:b}'.format(n)
        binary_iter = list(binary_string)
        return list(map(int, binary_iter))

    def helper_test_pair(self, a, b):
        binary_a = self.helper_int_to_binary(a)
        binary_b = self.helper_int_to_binary(b)
        if len(binary_a) == len(binary_b):
            res = binary_sum(binary_a, binary_b)
            exp = self.helper_int_to_binary(a + b)
            self.assertSequenceEqual(res, exp)
        
    def test_binary_sum(self):
        TEST_RANGE = 100
        for a in range(1, TEST_RANGE):
            for b in range(1, TEST_RANGE):
                self.helper_test_pair(a, b)


# Runner:
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)
