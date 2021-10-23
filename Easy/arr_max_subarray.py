"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1: Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6 Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2: Input: nums = [1]
Output: 1

Example 3: Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10^5
-10000 <= nums[i] <= 10000

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

2. Clarifications
3. Edge Cases

4. Approach1: dynamic sliding window. add curr value into sum, return max curr sum in subarray. Reset curr_sum if it
negative.
Time: O(n)
Space: O(1) aux space for vars only

Approach2: Use Divide and Conquer technique
Time:
Space:

"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return 0

    def max_subarray_sw(self, nums: List[int]) -> int:
        """
        Kadane algorithm
        :param nums: list of ints (can contain negative)
        :return: the max sub array of given list
        """
        cur_sum = 0
        best_sum = -10000
        for num in nums:
            cur_sum = max(0, cur_sum + num)
            best_sum = max(best_sum, cur_sum)
        return best_sum


if __name__ == '__main__':
    tests = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]
    for nums, expected in tests:
        result = Solution().maxSubArray(nums)
        res = Solution().max_subarray_sw(nums)
        assert res == expected
        print(result)