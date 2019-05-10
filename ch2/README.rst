.. Part of CLRS solutions by SweetPalma, 2019. See LICENSE for details.

=========
Chapter 2
=========
.. contents:: **The role of algorithms in computing**:
    :depth: 1


Exercise 2.1.1 - Insertion sort in action
=========================================

    Illustrate the operation of ``insertion_sort`` on the array ``arr = [31, 41, 59, 26, 41, 58]``.

Solution
--------
.. code ::
    
        -   J
    0: [31, 41, 59, 26, 41, 58]
        -   -   J
    1: [31, 41, 59, 26, 41, 58]
        +   -   -   J
    2: [31, 41, 59, 26, 41, 58]
                     +  J
    3: [27, 31, 41, 59, 41, 58]
                        +   J
    4: [27, 31, 41, 41, 59, 58]


Exercise 2.1.2 - Reversed insertion sort
========================================

    Rewrite the ``insertion_sort`` procedure to sort into nonincreasing instead of nondecreasing order.

Solution
--------
You can see a regular insertion sort below. In order to make it reversed, simply change ``arr[i] > key`` to ``arr[i] < key``. Yes, it is that easy.

.. code :: python

    def insertion_sort(arr): 
        for j in range(1, len(arr)):
            key = arr[j]
            i = j - 1
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i = i - 1
            arr[i + 1] = key


Exercise 2.1.3 - Linear search
==============================

    Write code for linear search, which scans through the sequence, looking for ``v``. Using a loop invariant, prove that your algorithm is correct. Make sure that your loop invariant fulfills the three necessary properties.

Invariant
---------
- **Initialization**: 
    Initially the subarray is an empty array, so none of its elements are equal to ``v``.

- **Maintenance**: 
    At each step we compare ``arr[i]`` with ``v``. If they are the same, we return ``i``, otherwise we continue to the next step. So, if the subarray ``arr[0 .. i − 1]`` does not contain ``v`` before the ``i``-th iteration, the subarray ``arr[0 .. i]`` will not contain ``v`` before the next iteration too.

- **Termination**: 
    Loop terminates at ``len(arr)``. Since ``i`` is increased by ``1``, we know that all elements have been checked and it has been found that ``v`` is not among them. Thus, we return ``None``.

Solution
--------
.. code :: python

    def linear_search(arr, target):
        for i in range(0, len(arr)):
            if arr[i] == target:
                return i
        return None


Exercise 2.1.4 - Binary sum
===========================

    Consider the problem of adding two ``n``-bit binary integers, stored in two ``n`` element arrays ``a`` and ``b``. The sum of the two integers should be stored in binary form in an ``(n + 1)`` element array ``c``. State the problem formally and write pseudocode for adding the two integers.

Invariant
---------

- **Initialization:**
    Initially we have an empty ``c`` list. Also we initialize a zero ``carry`` variable, containing the carry digit.

- **Maintenance:**
    Loop starts from the least significant digit. At each step we sum ``a[i]``, ``b[i]`` and ``carry``, storing the result into the temporary variable. If it is bigger than ``1`` (case when ``1 + 1 = 10``), we transfer the rest of it to the ``carry`` buffer. Then we push the resulting digit right into the beginning of the ``c`` list.

- **Termination:**
    Loop terminates at ``1``. Since ``i`` is decreased by ``1``, we know that all digits were added. The last thing we need to do is to flush the potentially non-zero ``carry`` buffer into the beginning of ``c`` and return the final result.

Solution
--------
.. code :: python

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


Exercise 2.2.1 - Theta function is easier than you think
========================================================
    
    Express the function ``(n^3) / 1000 + (n^3) * 100 + n * 100 + 3`` in terms of Θ-notation.

Solution
--------
It is fairly easy: just take part which has the fastest growing grate, which is ``Θ(n^3)``.


Exercise 2.2.2 - Selection sort
===============================

    Consider sorting ``n`` numbers stored in array ``arr`` by first finding the smallest element of ``arr`` and exchanging it with the element in ``arr[0]``. Then find the second smallest element of ``arr``, and exchange it with ``arr[1]``. Continue in this manner for the first ``n - 1`` elements of A. Write pseudocode for this algorithm, which is known as selection sort. What loop invariant does this algorithm maintain? Why does it need to run for only the first ``n - 1`` elements, rather than for all ``n`` elements? Give the best-case and worst-case running times of selection sort in Θ notation.

Solution
--------
Algorithm needs to be run ``n - 1`` times instead of ``n`` because the rest of the array is already sorted when ``j`` reaches it. Worst time complexity is ``Θ(n^2)`` (array is sorted in reversed order), best time complexity is ``Θ(n)`` (array is already sorted).

.. code :: python

    def selection_sort(arr):
        for j in range(0, len(arr) - 1):
            smallest = j
            for i in range(j + 1, len(arr)):
                if (arr[i] < arr[smallest]):
                    smallest = i
            arr[j], arr[smallest] = arr[smallest], arr[j]


Exercise 2.2.3 - Linear search revisited
========================================

    Consider linear search again. How many elements of the input sequence need to be checked on the average, assuming that the element being searched for is equally likely to be any element in the array? How about in the worst case? What are the average-case and worst-case running times of linear search in Θ-notation? Justify your answers.

Solution
--------
Assuming equal probability of occurrence ``1/n``, average number of elements which need to be checked is ``1/n * (1 + 2 + ... + n) = (n+1)/2``. That means that half of the elements are likely to be checked before it is found in the average case. Thus ``n / 2`` checks in average and ``n`` checks in the worst case. That means linear ``Θ(n)`` theta time.


Exercise 2.2.4 - Black magic optimization
=========================================

    How can we modify almost any algorithm to have a good best-case running time?

Solution
--------
First, we can modify it to handle the best-case efficiently. For example, if we modify merge-sort to check if the array is sorted and just return it. After that, we may perform a memoization trick for pure functions by storing the results of expensive function calls and returning the cached result when the same inputs occur again.


Exercise 2.3.1 - Merge sort in action
=====================================

    Illustrate the operation of merge sort on the array ``arr = [3, 41, 52, 26, 38, 57, 9, 49]``.

Solution
--------
.. code :: 

    0: [3, 41, 52, 26, 38, 57, 9, 49]

    1: [3] + [41] [52] + [26] [38] + [57] [9] + [49]

    2: [3, 41] + [26, 52] [38, 57] + [9, 49]

    3: [3, 26, 41, 52] + [9, 38, 49, 57]

    4: [3, 9, 26, 41, 59, 52, 57]


Exercise 2.3.2 - Merge without infinity
=======================================

    Rewrite the ``merge`` procedure so that it does not use sentinels, instead stopping once either array ``arr_left`` or ``arr_right`` has had all its elements copied back to ``arr`` and then copying the remainder of the other array back into ``arr``.

Solution
--------
In order to eleminate sentinel cards, we may check the number of untouched elements in left and right parts of array - and perform a fast-forward if no one is left.

.. code :: python

    def merge(arr, p, q, r):
        arr_left = arr[p:q+1]
        arr_right = arr[q+1:r+1]
        i = j = 0
        for k in range(p, r + 1):
            if j >= len(arr_right):
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


Exercise 2.3.3 - Mathematical induction
=======================================

    Use mathematical induction to show that when ``n`` is an exact power of ``2``, the solution of the following recurrence is ``T(n) = n * lg(n)``.

    .. code ::

        T(n) = 2,                if n = 2
        T(n) = 2 * T(n / 2) + n, if n = 2^k, k > 1 

Solution
--------
We must prove it for the best case first:

.. code ::

    T(2) = n * lg(n) = 2 * 1 = 2

Then we can prove the same for the inductive step:

.. code ::

    T(n / 2) = (n / 2) * lg(n / 2)
    T(n) = 2 * (n / 2) * lg(n / 2)
    T(n) = n * (lg(n - 1)) + n
    T(n) = n * lg(n) - n + n
    T(n) = n * lg(n)


Exercise 2.3.4 - Recurrence for insertion sort 
==============================================

    Insertion sort can be expressed as a recursive procedure as follows. In order to sort ``arr[0..n]``, we recursively sort ``arr[0..n - 1]`` and then insert ``arr[n]`` into the sorted array ``arr[0..n - 1]``. Write a recurrence for the running time of this recursive version of insertion sort.

Solution
--------
.. code ::

        T(n) = Θ(1),            if n = 1
        T(n) = T(n - 1) + Θ(n), if n > 1
        T(n) = Θ(n ^ 2)


Exercise 2.3.5 - Binary search
==============================

    Referring back to the searching problem, observe that if the sequence ``arr`` is sorted, we can check the midpoint of the sequence against ``v`` and eliminate half of the sequence from further consideration. Binary search is an algorithm that repeats this procedure, halving the size of the remaining portion of the sequence each time. Write pseudocode, either iterative or recursive, for binary search. Argue that the worst-case running time of binary search is ``Θ(lg(n))``.

Solution
--------
Search terminates when the range is empty ``low > high`` and terminate it successfully when ``v`` is found. Based on the comparison of ``v`` to the middle element in the range, search continues with the halved range. The recurrence in such case is ``T(n) = T(n / 2) + Θ(1)``, whose solution is ``T(n) = Θ(lg(n))``.

.. code :: python

    def binary_search(arr, v, low, high):
        while low <= high:
            mid = math.floor((low + high) / 2)
            if arr[mid] == v:
                return mid
            elif v > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return None


Exercise 2.3.6 - Insertion sort optimization
============================================

    Observe that the while loop of lines ``5 - 7`` of the ``insertion_sort`` procedure uses a linear search to scan (backward) through the sorted subarray ``arr[0..j - 1]``. Can we use a binary search instead to improve the overall worst-case running time of insertion sort to ``Θ(n * lg(n))``?

Solution
--------
We may use binary search in order to find an appropriate position for ``n``-th item. Unfortunately, insertion still requires element shift, which takes ``Θ(n)`` operations, causing ``Θ(n ^ 2)`` complexity in total.


Exercise 2.3.7 - Looking for a pair
===================================

    Describe a ``Θ(n * lg(n))`` time algorithm that, given a set ``arr`` of ``n`` integers and another integer ``x``, determines whether or not there exist two elements in ``arr`` whose sum is exactly ``x``.

Solution
--------
Target algorithm is fairly simple. First, sort the input ``arr`` in a ``Θ(n * lg(n))`` time. Then, for each element ``y`` in ``arr``, perform a binary search for ``x - y``. Each binary search takes ``O(lg(n))`` and there are ``n`` most of them, so the total lookup time is ``Θ(n * lg(n))``.

.. code :: python

    def pair_search(arr, x):
        merge_sort(arr, 0, len(arr) - 1)
        for y in arr:
            i = binary_search(arr, x - y, 0, len(arr) - 1)
            if i != None:
                return True
        return False

Problem 2.1 - Mixing merge and insertion sort
=============================================

    Although merge sort runs in ``Θ(n * lg(n))`` worst-case time and insertion sort runs in ``Θ(n^2)`` worst-case time, the constant factors in insertion sort can make it faster in practice for small problem sizes on many machines. Thus, it makes sense to coarsen the leaves of the recursion by using insertion sort within merge sort when subproblems become sufficiently small. Consider a modification to merge sort in which ``n / k`` sublists of length ``k`` are sorted using insertion sort and then merged using the standard merging mechanism, where ``k`` is value to be determined.

    1) Show that the ``n / k`` sublists, each of length ``k``, can be sorted by insertion sort in ``Θ(n * k)`` worst-case time. 

    2) Show that the sublists can be merged in ``Θ(n * lg(n/k))`` worst-case time.

    3) Given that the modified algorithm runs in ``Θ(n*k + n*lg(n/k))`` worst-case time, what is the largest asymptotic value of ``k`` as a function of ``n`` for which the modified algorithm has the same asymptotic running time as standard merge sort? 

    4) How should ``k`` be chosen in practice?

Solution #1
-----------
Insertion sort takes ``Θ(k^2)`` time for ``k`` element list in the worst case. Thus, sorting ``n/k`` sublists would take ``Θ((k^2) * n/k) = O(n/k)``.

Solution #2
-----------
Imagine two lists could be merged in a constant time - we could achieve ``Θ(lg(n/k))`` speed by taking 2 sublists at a time and merging them in pyramid-like manner: ``[[a, b], [c, d]] -> [ab, bc] -> [abcd]``. But merge takes ``Θ(n)`` time itself, causing ``Θ(n * lg(n/k))`` complexity in total.

Solution #3
-----------
Stanard merge sort runs ``Θ(n * lg(n))`` and our modified algorithm does the same in ``Θ(nk + nlg(n/k))``. In order to find that value, we need to solve the equation ``Θ(n*k + n*lg(n/k)) = Θ(n * lg(n))``, what gives us ``k = Θ(lg(n))``. That happens because ``k`` can't be a more then ``Θ(lg(n))``, i.e. can't have a higher order term than ``lg(n)``, for otherwise the left-handed expression would not be ``Θ(n * lg(n))``.

Solution #4
-----------
It depends on constant factors, so in practice it is necessary to run benchmark tests in order to determine how large ``k`` should be.


Problem 2.2 - Bubble sort analysis
==================================

    Bubblesort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order.

    .. code :: python

        def bubble_sort(arr):
            for i in range(1, len(arr)):
                for j in reversed(range(i, len(arr))):
                    if arr[j] < arr[j - 1]:
                        arr[j], arr[j - 1] = arr[j - 1], arr[j]

    1) Let ``arr'`` denote the output of ``bubble_sort(arr)``. To prove that ``bubble_sort`` is correct, we need to prove that it terminates and that ``arr'[0] < arr'[1] < ... < arr'[n]``, where ``n`` is length of ``arr``. In order to show that ``bubble_sort`` actually sorts, what else do we need to prove? The next two parts will prove inequality (2.3).

    2) State precisely a loop invariant for the for loop in lines 3–5, and prove that this loop invariant holds. Your proof should use the structure of the loop invariant proof presented in this chapter.

    3) Using the termination condition of the loop invariant proved in part (2), state a loop invariant for the for loop in lines 1–5 that will allow you to prove inequality (2.3). Your proof should use the structure of the loop invariant proof presented in this chapter.

    4) What is the worst-case running time of bubblesort? How does it compare to the running time of insertion sort?


Solution #1
-----------
We need to prove that elements of ``arr'`` for a permutation of the elements of original ``arr``.

Solution #2
-----------
    
    At the start of each iteration, the subarray ``arr[j .. n]`` consists of elements originally in ``arr[j .. n]`` before entering the loop, but possibly in a different order. The first element is the smallest of them.


- **Initialization:**
    Initially the array contains only last element ``arr[n]`` and trivially this is the smallest element.

- **Maintenance:**
    We iterate over the subarray, ensuring that ``arr[j - 1]`` is smaller than ``arr[j]``, swapping them if needed. Thus, in the end of iteration, the first element is the smallest one.

- **Termination:**
    Loop terminates when ``j = i + 1``. This suggests that after the loop terminates, ``arr[i]`` is the smallest element in the subarray.


Solution #3
-----------
    
    At the start of each iteration, the subarray ``arr[0 .. i - 1]`` consists of elements that are smaller than the elements in the subarray ``arr[0 .. n]`` in sorted order.

- **Initialization:**
    Initially the array contains only last element ``arr[n]`` and trivially this is the smallest element.

- **Maintenance:**
    Due to the inner loop invariant, ``arr[i]`` becomes the smallest element in the subarray ``arr[i .. n]`` and is less than or equal to all of the elements in the subarray ``arr[i + 1 .. n]``.

- **Termination:**
    Loop terminates when ``i = n``. This suggests that the subarray ``arr[0 .. n - 1]`` is in sorted order, where each element is less than or equal to elements in the subarray ``arr[i .. n]``, which only consists of the final element. Thus, the array ``arr[0 .. n]`` is sorted.

Solution #4
-----------
At the worst case, bubble sort will iterate over each element, performing ``n`` comparisons and swaps. Thus, the worst running case is ``Θ(n^2)``. It is also important to note that bubble sort performs a way more swaps than insertion sort does, so with the same time complexity it runs slower, making it completely impractical.
    

Problem 2.3 - Horner's rule analysis
====================================

    The following code fragment implements Horner's rule for evaluating a polynomial: ``P(x) = Σ(n, k=0, arr[k] * x^k) = arr[0] + arr[1] * x + arr[2] * (x ^ 2) + ... + arr[n] * (x ^ n)``.

    .. code :: python

        def horner_rule(arr, x):
            y = 0
            for i in reversed(range(0, len(arr))):
                y = arr[i] + x * y
            return y

    1) In terms of Θ-notation, what is the running time of this code fragment for Horner's rule?

    2) Write pseudocode to implement the naive polynomial-evaluation algorithm that computes each term of the polynomial from scratch. What is the running time of this algorithm? How does it compare to Horner's rule?

    3) Consider the following loop invariant: At the start of each iteration of the for loop of lines 3-4: ``y = Σ(n - (i + 1), k=0, arr[k + i + 1] * (x^k))``. Interpret a summation with no terms as equaling 0. Your proof should follow the structure of the loop invariant proof presented in this chapter and should show that, at termination, ``Σ(n, k=0, arr[k] * x^k)``.

    4) Conclude by arguing that the given code fragment correctly evaluates a polynomial characterized by the coefficients ``arr[0], arr[1], ... arr[n]``.

Solution #1
-----------
Optimal solution performs linear iteration without nested loops and recursion, so expected complexity is ``Θ(n)``.

Solution #2
-----------
Complexity of naive implmentation is ``Θ(n^2)``, what is caused by a heavy nested loop.

.. code :: python

    def naive_horner_rule(arr, x):
        y = 0
        for k in range(0, len(arr)):
            temp = 1
            for i in range(0, k):
                temp = temp * x
            y = y + arr[k] * temp
        return y

Solution #3
-----------
.. This task is really horrible. It makes me cry somtimes, why math is so hard?

- **Initialization:**
    It is pretty trivial, since the summation has no terms which implies ``y = 0``.

- **Maintenance:**
    By using the loop invariant, in the end of the ``i``-th iteration we are going to have:

    .. code :: 

        y = arr[i] + x * Σ(n - (i + 1), k=0, arr[k + i + 1] * (x^k))
        y = arr[i] * x + Σ(n - (i - 1), k=0, arr[k + i + 1] * (x^(k + 1))
        y = arr[i] * x + Σ(n - i, k=1, arr[k + i] * (x^k)
        y = Σ(n - i, k=0, arr[k + i] * (x^k)

- **Termination:**
    Loop terminates at ``i = -1``. So we can substitute:

    .. code ::

        y = Σ(n - (i + 1), k=0, arr[k + i + 1] * (x^k))
        y = Σ(n, k=0, arr[k] * x^k)

Solution #4
-----------
When Horner's rule loop terminates it successfully evaluates polynom it is inteded too. That implies that algorithm is correct.


Problem 2.4 - Inversions 
========================

    Let ``arr[0 .. n]`` be an array of n distinct numbers. If ``i < j`` and ``arr[i] > arr[j]``, then the pair ``(i, j)`` is called an inversion of ``arr``.

    1) List the five inversions of the array ``[2, 3, 8, 6, 1]``.

    2) What array with elements from the set ``[1, 2, ..., n]`` has the most inversions? How many does it have? 

    3) What is the relationship between the running time of insertion sort and the number of inversions in the input array? Justify your answer. 

    4) Give an algorithm that determines the number of inversions in any permutation on ``n`` elements in ``Θ(n * lg(n))`` worst-case time. (Hint: Modify merge sort).


Solution #1
-----------
Invertion values are ``[[1, 5], [3, 1], [8, 6], [8, 1], [6, 1]]``. Invertions are ``[[0, 4], [1, 4], [2, 3], [2, 4], [3, 4]]`` (indexing starts from zero).

Solution #2
-----------
We need to minimze ``(i, arr[j])`` and maximize ``(j, arr[i])`` what could be achieved by passing a reversed array ``[n, n - 1, n - 2, ..., 1]``. That will cause ``1, 2, ..., n = (n * (n - 1)) / 2`` inversions in total.

Solution #3
-----------
We may take a look at the code of insertion sort and notice that bigger count of inversions is causing more iterations of the inner while loop.

Solution #4
-----------
Problem explanation hints us about similarity to the merge sort, what implies "divide and conquer" algorithm. That means it is possible write an algorithm, which is going to recursively divide the array into halfs and count number of inversions in the sub-arrays. This will require ``lg(n)`` steps and ``Θ(n)`` operations during each, causing total complexity ``Θ(n * lg(n))``.

.. code :: python 

    def modified_merge_sort(arr, p, r):
        inversions = 0
        if p < r:
            q = math.floor((p + r) / 2)
            inversions = inversions + modified_merge_sort(arr, p, q)
            inversions = inversions + modified_merge_sort(arr, q + 1, r)
            inversions = inversions + modified_merge(arr, p, q, r)
        return inversions

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

