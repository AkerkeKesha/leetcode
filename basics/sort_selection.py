"""
The selection sort algorithm sorts an array by repeatedly finding the minimum element
 (considering ascending order) from unsorted part and putting it at the beginning.
 The algorithm maintains two subarrays in a given array.
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.
In every iteration of selection sort,
the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
"""
from typing import List


def select_sort(array: List[int]) -> None:
    """
    Time: O(N^2) due to nested loop
    Space: O(1) in-place swapping, sort array in-place
    :param array: list of integers to sort
    :return:
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == '__main__':
    lst = [64, 25, 12, 22, 11]
    print(lst)
    select_sort(lst)
    print(lst)

