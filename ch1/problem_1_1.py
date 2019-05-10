#!/usr/bin/env python3
# Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.
import math


# Helper:
class ProblemSizeCalculator:

    def max_for_log2(self, n):
        ''' Inverse root for lg(n) is (2 ^ n). '''
        return 2 ** n

    def max_for_sqrt(self, n):
        ''' Inverse function for sqrt(n) is (n ^ 2). '''
        return math.floor(n ** 2)

    def max_for_n(self, n):
        ''' Inverse function for (n) is (n) itself. '''
        return n

    def max_for_pow2(self, n):
        ''' Inverse function for (n ^ 2) is sqrt(n). '''
        return math.floor(math.sqrt(n))

    def max_for_pow3(self, n):
        ''' Inverse function for (n ^ 3) is cbrt(n). '''
        return math.floor(math.pow(n, 1 / 2.99999999999))

    def max_for_2pow(self, n): 
        ''' Inverse function for (2 ^ n) is lg(n). '''
        return math.floor(math.log2(n))

    def max_for_fac(self, n):
        ''' Manual linear search for (n!). '''
        x = 1
        while math.factorial(x) < n:
            x = x + 1
        return x - 1

    def max_for_nlog2(self, n):
        ''' Manual binary search for (n * lg(n)). '''
        step = 100000000
        x = 1
        while step > 1:
            while x * math.log2(x) < n:
                x = x + step
            x = x - step
            step = step / 2
        return x

    def calculate_for_second(self, method):
        ''' One second is 10^6 microseconds. '''
        return method(10 ** 6)

    def calculate_for_minute(self, method):
        ''' One minute is 6 * 10^7 microseconds. '''
        return method(6 * (10 ** 7))

    def calculate_for_hour(self, method):
        ''' One hour is 3.6 * 10^9 microseconds. '''
        return method(3.6 * (10 ** 9))

    def calculate_for_day(self, method):
        ''' One day is 8.64 * 10^10 microseconds. '''
        return method(8.64 * (10 ** 10))

    def calculate_for_month(self, method):
        ''' One month is 2.592 * 10^12 microseconds. '''
        return method(2.592 * (10 ** 12))

    def calculate_for_year(self, method):
        ''' One year is 3.1536 * 10^13. microseconds. '''
        return method(3.1536 * (10 ** 13))

    def calculate_for_century(self, method):
        ''' One centure is 3.1536 * 10^15 microseconds. '''
        return method(3.1536 * (10 ** 15))

    def pretty(self, n, len=10):
        ''' Pretty output for huge numbers. '''
        if n > 100000000000:
            return '%.5E' % n
        else:
           return '%d' % n


# Solution & Runner:
if __name__ == '__main__':
    calc = ProblemSizeCalculator()
    # calc.max_for_log2 is not included due to computation complexity
    methods = [
        calc.max_for_sqrt,
        calc.max_for_n,
        calc.max_for_nlog2,
        calc.max_for_pow2,
        calc.max_for_pow3,
        calc.max_for_2pow,
        calc.max_for_fac,
    ]
    for method in methods:
        print('Calculation for:', method.__name__)
        print('- Second: \t', calc.pretty(calc.calculate_for_second(method)))
        print('- Minute: \t', calc.pretty(calc.calculate_for_minute(method)))
        print('- Hour:   \t', calc.pretty(calc.calculate_for_hour(method)))
        print('- Day:    \t', calc.pretty(calc.calculate_for_day(method)))
        print('- Month:  \t', calc.pretty(calc.calculate_for_month(method)))
        print('- Year:   \t', calc.pretty(calc.calculate_for_year(method)))
        print('- Century:\t', calc.pretty(calc.calculate_for_century(method)))
        print()
