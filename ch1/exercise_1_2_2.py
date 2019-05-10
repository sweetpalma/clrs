#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import unittest
import math


# Solution:
def lookup():
    n = 1
    while abs(8 * math.log2(n) - n) >= 1:
        n = n + 1
    return n


# Runner:
if __name__ == '__main__':
    print(lookup())
