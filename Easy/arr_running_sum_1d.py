""""
1. Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6

2. Clarifications:
- How big is the nums array? size max. 1000
- How big are elements? Could they be negative? see constraints, yes
- How to handle empty array as input? Just return []
- Can I assume None is not passed as input?

3. Test Cases:

4. Approach1: Use naive approach traverse each element add and append to result
Time: O(N) to traverse nums
Space: O(N) to save the resulting array

"""
from typing import List

class Solution:

    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        result = []
        for num in nums:
            running_sum += num
            result.append(running_sum)
        return result


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4], [1, 3, 6, 10]),
        ([1,1,1,1,1], [1,2,3,4,5]),
        ([3,1,2,10,1], [3,4,6,16,17]),
        ([], []),
    ]
    for nums, expected in tests:
        result = Solution().runningSum(nums)
        assert result == expected
