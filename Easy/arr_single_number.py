"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1


Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

2. Clarification
3. Edge cases
4. Approach1: Create a map, return key with value = 1.
Time: O(N)
Space: O(N) to store the map
"""


class Solution:

    def singleNumber(self, nums) -> int:
        table = {}
        for num in nums:
            table[num] = table.get(num, 0) + 1
        for t in table:
            if table[t] == 1:
                return t


if __name__ == '__main__':
    tests = [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1)
    ]
    for nums, expected in tests:
        sol = Solution().singleNumber(nums)
        assert sol == expected
