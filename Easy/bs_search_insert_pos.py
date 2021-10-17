"""
Given a sorted array of distinct integers and a target value,
 return the index if the target is found.
 If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1: Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2: Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3: Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4: Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5: Input: nums = [1], target = 0
Output: 0


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

2. Clarifications
3. Edge cases
4. Approach1:
Time:
Space:

"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    tests = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1], 0, 0),
    ]
    for nums, target, expected in tests:
        result = Solution().searchInsert(nums, target)
        assert result == expected
