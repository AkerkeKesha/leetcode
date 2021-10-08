"""
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths.
If it is impossible to form any triangle of a non-zero area, return 0.
The necessary and sufficient condition for these lengths to form a triangle of non-zero area is
 a + b > c.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0. Cannot form a triangle because a + b > c does not work

Example 3:
Input: nums = [3,2,3,4]
Output: 10

Example 4:
Input: nums = [3,6,2,3]
Output: 8


Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106

2. Clarifications

3. Edge cases

4. Approach1: Sort list. For any c in the array, we choose the largest possible a and b, such that a ≤ b ≤ c:
ie. two adjacent values. If this forms a triangle, we return the answer.
Time: O(NlogN) to sort
Space: O(1)

"""
from typing import List
from basics.sort_selection import select_sort


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        select_sort(nums)
        for i in range(len(nums)-3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


if __name__ == '__main__':
    tests = [
        ([2, 1, 2], 5),
        ([1, 2, 1], 0),
        ([3, 2, 3, 4], 10),
        ([3, 6, 2, 3], 8),
    ]
    for nums, expected in tests:
        result = Solution().largestPerimeter(nums)
        assert result == expected