"""
Given: sorted array of int (important), n elements
Function: to find given element, x in this n array
Binary Search Algo: Search a sorted array by repeatedly dividing the search interval in half.
Begin with an interval covering the whole array. If the value of the search key is less than
the item in the middle of the interval, narrow the interval to the lower half.
Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

Recursive:
Iterative:

"""
from typing import List


def binary_search(array: List[int], left: int, right: int, x: int) -> int:
    """
    Time: O(logN)
    Space: O(logN) recursive call stack space
    :param array: list of sorted integers
    :param left:
    :param right:
    :param x:
    :return: index of x in arr if present, else -1
    """
    if right >= left:
        mid = left + (right - left) // 2  # to avoid overflow error
        if x == array[mid]:
            return mid
        elif x < array[mid]:
            return binary_search(array, left, mid - 1, x)
        else:
            return binary_search(array, mid + 1, right, x)
    else:
        return -1


def binary_search_iter(array: List[int], x: int) -> int:
    """
    Time: O(logN)
    Space: O(1)
    :param array: sorted list of ints
    :param x: int to search for
    :return: index of x or -1 if not found
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == x:
            return mid
        elif x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


if __name__ == '__main__':
    tests = [
        ([11, 11, 12, 22, 25, 64, 100], 25, 4),
        ([1, 2, 3, 4], 0, -1),
    ]
    for array, x, expected in tests:
        result = binary_search(array, left=0, right=len(array)-1, x=x)
        another = binary_search_iter(array, x)
        assert result == expected
        assert another == expected
