.. Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.

=========
Chapter 1
=========
.. contents:: **The role of algorithms in computing**:
    :depth: 1


Exercise 1.1.1 - Sorting and convex hull application
====================================================

    Give a real-world example in which one of the following computational problems appears: sorting, determining the best order for multiplying matrices, or finding the convex hull.

Convex Hull
-----------
It may be used for solving the smallest box problem (finding a smallest rectangular box for containing a convex hull polygon), or danger zone targeting (enlosing a set of points in the smallest possible polygon).

Sorting
-------
Sorting may be used for solving ordering operations (used basically everywhere), ranging (different stores, searches, etc) and as a part of a other algorithms.


Exercise 1.1.2 - Vital metrics
==============================

    Other than speed, what other measures of efficiency might one use in a real-world setting?

Execution time
--------------
Execution time can be determined as estimate of running time as function of the size of input data. Note that sometimes it can be hard to analyze complex algorithms.

Parallelism
-----------
In a modern world of multi-core processors it is important to take into account degree of parallelism of a certain algorithms - some of them parallelize pretty well, others don't.

Memory consumption
------------------
There are different aspects of memory consumption - sometimes faster algorithm may need more of space.

- Algorithm code memory.
- Input data set memory.
- Output data set memory.
- Temporary data memory.


Exercise 1.1.3 - Lovely data structures
=======================================

    Select a data structure that you have seen previously, and discuss its strengths and limitations.

Linked List
-----------
A linked list is a linear data structure where each element is a separate object. Each element (we will call it a node) of a list is comprising of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list, the rest is called tail.

----
Pros
----
- Element insertion is done in constant time.
- Easy to traverse from head to tail.

----
Cons
----
- Memory overhead caused by need to store tail pointer.
- Element indexing is done by traversing.
- Impossible to traverse backwards.


Exercise 1.1.4 - Travelling salesman and shortest path
======================================================

    How are the shortest-path and traveling-salesman problems given above similar? How are they different?

Similarities
------------
- Both deal with graphs.

Differences
-----------
- The TSP solution will necessarily repeat a node in its path, while a shortest path will not.
- Shortest path can be done in polynominal time, and travelling salesman is an NP-full problem.
- TSP can't be break down in similar but smaller sub-problems.


Exercise 1.1.5 - Good solutions and the best solutions
======================================================

    Come up with a real-world problem in which only the best solution will do. Then come up with one in which a solution that is "approximately" the best is good enough.

Best
----
- Finding a binary sum.
- Finding a greatest common delimiter of two numbers.
- Sorting a list.

Good
----
- Finding the solution of differential equations.
- Numerical intergration.
- Raytracing problem.


Exercise 1.2.1 - Complex algorithms in daily life
=================================================

    Give an example of an application that requires algorithmic content at the application level, and discuss the function of the algorithms involved.

Video games
-----------
Rendering (matrix multiplication, raytracing, inverse square root, etc), collision detection (convex hull and raytracing), physics (convex hull and black magic), etc.

Web browsing
------------
Virtual DOM rendering (simplified linear tree comparison), building a rendering tree (various graph algorithms and optimizations), etc.

Map navigation
--------------
Pathfinding (shortest path), time estimation (shortest path, weight calculation, etc).


Exercise 1.2.2 - Merge and insertion
====================================

    Suppose we are comparing implementations of insertion sort and merge sort on the same machine. For inputs of size n, insertion sort runs in ``(8 *(n^2))`` steps, while merge sort runs in ``(64 * n * lg(n))`` steps. For which values of n does insertion sort beat merge sort?

Solution
--------
We can use Lambert W function to solve final equation, but simple algebraic solution is much simplier - and it gives us result of ``43``.

.. code ::
    
    8 * (n ^ 2) = 64 * n * lg(n)
    n * n = 8 * n * lg(n)
    8 * lg(n) = n
    8 * lg(n) - n = 0


Exercise 1.2.3 - Exponential and polynominal
============================================

    What is the smallest value of ``n`` such that an algorithm whose running time is ``(100 * (n ^ 2))`` runs faster than an algorithm whose running time is ``(2 ^ n)`` on the same machine?

Solution
--------
First, we should admit that ``(2^n)`` is an exponential function, whereas ``(100 * (n^2))`` is a polynominal function. That means that when ``n`` is large enough, it will be the case that ``(2^n) > (100 * (n^2))``. So we can find a simple algebraic solution here too, which equals to ``14``.


Problem 1.1 - Execution time in action
======================================

    For each function ``f(n)`` and time ``t`` in the following table, determine the largest size ``n`` of a problem that can be solved in time ``t``, assuming that the algorithm to solve the problem takes ``f(n)`` microseconds.

Solution
--------
For each time ``T``, and each function ``f(n)``, you are required to find the maximal integer ``n`` such that ``f(n) <= T``. So the task is to find an inverse of each function - example of such computation can be seen below:

.. code :: 

    Given:
    T = 1000s (10^6us)
    f = (n ^ 2)

    Solution:
    n ^ 2 <= (10^6)
    n <= sqrt(10^6)
    n <= 1000

================ ================ ================ ================ ================ ================ ================ =================
Item             Second           Minute           Hour             Day              Month            Year             Century
================ ================ ================ ================ ================ ================ ================ =================
O(lg(n))         2^(1.00000E+12)  2^(3.60000E+15)  2^(1.29600E+19)  2^(7.46496E+21)  2^(6.71846E+24)  2^(9.94519E+26)  2^(9.94519E+30)
O(sqrt(n))       1.00000E+12      3.60000E+15      1.29600E+19      7.46496E+21      6.71846E+24      9.94519E+26      9.94519E+30
O(n)             1000000          60000000         3600000000       86400000000      2.59200E+12      3.15360E+13      3.15360E+15
O(n * lg(n))     62745            2801417          133378058        2755147511       71870856403      7.97634E+11      6.86110E+13
O(n ^ 2)         1000             7746             60000            293938           1609968          5615692          56156922
O(n ^ 3)         100              391              1532             4420             13736            31593            146645
O(2 ^ n)         19               25               31               36               41               44               51
O(n!)            9                11               12               13               15               16               17
================ ================ ================ ================ ================ ================ ================ =================
