"""
1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


2. Clarification:
- if pair does not exist? Not possible, assume always 1 pair exists
- numbers are all non-negative? Not really, negative is possible and that is OK
- how big is the num array?

3. Test cases:
- try mix of numbers, e.g  [-5, -4, 4], 0 return [1, 2]
4. Approach1:
Time: O(N)
Space: O(N) dict is used, i.e. hash map
"""
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # complements map contains the num as key and its index as key
        complements = {}
        for curr_ind, curr_num in enumerate(nums):
            complement = target - curr_num
            if complement in complements:  # if complement seen already, return
                return [complements[complement], curr_ind]
            else:
                complements[curr_num] = curr_ind


if __name__ == '__main__':
    tests = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-5, -4, 4], 0, [1, 2]),
    ]
    for nums, target, expected in tests:
        result = Solution().twoSum(nums, target)
        assert(result == expected)

