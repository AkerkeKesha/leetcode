"""
In insertion sort, we move many elements. The idea of shellSort is to allow exchange of far items.
In shellSort, we make the array h-sorted for a large value of h.
We keep reducing the value of h until it becomes 1.
An array is said to be h-sorted if all sublists of every h’th element is sorted.
"""
from typing import List


def shell_sort(array: List[int]) -> None:
    """
    Time: O(N^2)
    Space: O(1) in place
    :param array: list of integers to sort
    :return:
    """
    gap = len(array) // 2

    while gap > 0:
        i, j = 0, gap

        while j < len(array):

            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
            i += 1
            j += 1

            # much like insertion sort: look back from ith index to the left
            # swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if array[k - gap] > array[k]:
                    array[k - gap], array[k] = array[k], array[k - gap]
                k -= 1

        gap //= 2


if __name__ == '__main__':
    lst = [64, 25, 12, 22, 11]
    print(lst)
    shell_sort(lst)
    print(lst)