"""
Bubble: simplest sort algo. It works by repeatedly swapping the adjacent wrong elements.
"""
from typing import List


def bubble_sort(array: List[int]) -> None:
    """
    Time: O(N^2) nested loop to check adjacent elements, even if the array is sorted already
    Space: O(1) aux space
    :param array: list of integers to sort
    :return:
    """
    n = len(array)
    for i in range(n):  # need to pass 1, 2, 3...n times
        for j in range(0, n - i - 1):  # for i = 0, 1, 2, ...n then j = 0, ... n-1 then j = 0, ..n-2
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


if __name__ == '__main__':
    lst = [64, 34, 25, 12, 22, 11, 25, 90]
    print(lst)
    bubble_sort(lst)
    print(lst)
