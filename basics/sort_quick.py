"""
It is alse based on Divide and Conquer algorithm.
It picks an element as pivot and partitions the given array around the picked pivot.
"""
from typing import List


def partition(array: List[int], left:int, right:int) -> int:
    return -1


def _quick_sort(array: List[int], left:int, right:int) -> List[int]:
    return []


def quick_sort(array: List[int]) -> List[int]:
    """
    Time: O(NlogN), worst case O(N^2)
    Space: O(N)
    :param array: list of integers to sort
    :return:
    """
    return _quick_sort(array, 0, len(array)-1)


if __name__ == '__main__':
    lst = [64, 25, 12, 22, 11, 11, 100]
    print(lst)
    print(f"sorted: {quick_sort(lst)}")

