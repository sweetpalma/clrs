#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import math


# Solution:
def lookup():
    n = 1
    while (2 ** n) < (100 * (n ** 2)):
        n = n + 1
    return n - 1


# Runner:
if __name__ == '__main__':
    print(lookup())
