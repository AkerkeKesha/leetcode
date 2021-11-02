"""
Given an array of integers nums, sort the array in ascending order.

Ex1
Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Ex2
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Constraints:
1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
Duplicates are possible

Clarifications:
1. Any constraints in terms of time/space complexity
2. Are we allowed to use standard sort functions? No, implement merge-sort


Test Cases:


Approach 1
Time: O(nlogn). But the worst case O(n^2)
Space:

Tim Sort used in Java, Python.

"""
from typing import List


class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    def merge_sort(self, nums: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    test_cases = [
        ([5, 2, 3, 1], [1, 2, 3, 5]),
        ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),

    ]
    for sample_array, expected_array in test_cases:
        sorted_array = Solution().sortArray(sample_array)
        assert sorted_array == expected_array




