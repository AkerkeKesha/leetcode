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
import collections


class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        element_counter = {}
        for num in nums:
            element_counter[num] = element_counter.get(num, 0) + 1
        return max(element_counter, key=element_counter.get)

    def majority_element(self, nums) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


if __name__ == '__main__':
    tests = [
        ([-10], -10),
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([2, 2, 1, 1, 1, 2, 2, 1, 1], 1),
    ]
    for nums, expected in tests:
        result = Solution().majorityElement(nums)
        result2 = Solution().majority_element(nums)
        assert expected == result
        assert result2 == expected

