"""
 Insertion Sort: Values from unsorted part is picked and placed at the sorted position.
 the key starts at array[1] then compared to array[0...i-1]. Elements greater than key are
 moved to one element ahead

 """
from typing import List


def insert_sort(array: List[int]) -> None:
    """
    Time: O(N^2)
    Space: O(1) in place swapping
    :param array: list of integers to sort
    :return:
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


if __name__ == '__main__':
    lst = [34, 23, 1, 24, 75, 33, 54, 8]
    print(lst)
    insert_sort(lst)
    print(lst)
