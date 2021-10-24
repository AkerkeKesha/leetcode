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

Approach 2: Use DAC technique to partition array into two. If we know the majority element in the left and right halves
of an array, we can determine which is the global majority element in linear time.
Time: O(NlogN)
Space: O(logN)

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

    def majority_element_recursive(self, nums, start, end) -> int:
        # base case 1 number, that is the majority element
        if start == end:
            return nums[start]
        # recurse on left and right halves
        mid = (end + start) // 2
        left = self.majority_element_recursive(nums, start, mid)
        right = self.majority_element_recursive(nums, mid + 1, end)
        # case when both sides agree on the majority element
        if left == right:
            return left
        # otherwise find the winner
        count_left = sum(1 for i in range(start, end+1) if nums[i] == left)
        count_right = sum(1 for i in range(start, end+1) if nums[i] == right)
        return left if count_left > count_right else right

    def majority_element_dac(self, nums: List[int]) -> int:
        return self.majority_element_recursive(nums=nums, start=0, end=len(nums)-1)


if __name__ == '__main__':
    tests = [
        ([-10], -10),
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([2, 2, 1, 1, 1, 2, 2, 1, 1], 1),
    ]
    for nums, expected in tests:
        result = Solution().majorityElement(nums)
        result2 = Solution().majority_element_dac(nums)
        assert expected == result
        assert result2 == expected

