"""
1. Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

2. Clarifications
- Does majority element always exist? Yes
- Empty list? Return empty
- Can elements be negative? Yes
- How big are elements? How big is the array?

3. Test Cases:
- single element

4. Approach 1: Dictionary to keep count of current num, return the key which has the max value in this dict
Time: O(N) traverse list, get/search in dict is constant
Space: O(N) to store the dict

"""
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        element_counter = {}
        for num in nums:
            if num in element_counter:
                element_counter[num] += 1
            else:
                element_counter[num] = 0
        return max(element_counter, key=element_counter.get)


if __name__ == '__main__':
    tests = [
        ([-10], -10),
        ([3,2,3], 3),
        # size = 3, freq = 2
        ([2,2,1,1,1,2,2], 2),
        # size = 7, freq = 4
        ([2, 2, 1, 1, 1, 2, 2, 1, 1], 1),
        # size = 9, freq = 5
    ]
    for nums, expected in tests:
        result = Solution().majorityElement(nums)
        assert expected == result

