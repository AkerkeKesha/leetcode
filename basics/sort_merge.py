"""
Merge sort is Divide and Conquer Algo, which uses both recursive and iterative approaches in its implementation.
It uses merge_sort to recursively divide array until single elements are left. At the end merge() function is applied in
order merge two sorted halves.
Pseudo code:
MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
The merge(arr, l, m, r) is key process that assumes that
arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.
"""
from typing import List


def merge(array, arr_left, arr_right) -> List[int]:
    """
    Time: O(N) to merge two arrays
    :param array: original input
    :param arr_left: sorted left sub-array
    :param arr_right: sorted right sub-array
    :return:
    """
    left_pointer, right_pointer, position = 0, 0, 0
    # fill array[position] from 0...n with smaller elements from two sub-arrays
    while left_pointer < len(arr_left) and right_pointer < len(arr_right):
        if arr_left[left_pointer] < arr_right[right_pointer]:
            array[position] = arr_left[left_pointer]
            left_pointer += 1
        else:
            array[position] = arr_right[right_pointer]
            right_pointer += 1
        position += 1
    # elements left on the left sub-array
    while left_pointer < len(arr_left):
        array[position] = arr_left[left_pointer]
        left_pointer += 1
        position += 1
    # elements left on the right sub-array
    while right_pointer < len(arr_right):
        array[position] = arr_right[right_pointer]
        right_pointer += 1
        position += 1
    return array


def merge_sort(array: List[int]) -> List[int]:
    """
    Time: O(N * logN) we divide array into half in every step, which is log n
    and the number of steps can be represented by log n + 1(at most).
    Then perform a single step operation to find out the middle of any subarray, i.e. O(1).
    And to merge the subarrays, made by dividing the original array of n elements, a running time of O(n) will be required.
    Space: O(N) aux space to store array_left, array_right
    :param array: list of integers to sort
    :return:
    """
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(array, left, right)


if __name__ == '__main__':
    lst = [12, 11, 13, 5, 6, 7]
    print(lst)
    merge_sort(lst)
    print(f"Sorted array is:{lst}")
