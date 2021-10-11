"""
Given an array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
where 1 <= answer[0] < answer[1] <= numbers.length.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]

2. Clarification
- non-negative numbers?
- does input fit into memory?

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.

3. Test Cases
4. Approach 1: use two pointer from both ends if the sum of pointed numbers is less than target
Time:
Space:
"""
from typing import List


class Solution:

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        head = 0
        tail = len(nums) - 1
        while head < tail:
            if nums[head] + nums[tail] == target:
                return [head + 1, tail + 1]
            elif nums[head] + nums[tail] < target:
                head += 1
            else:
                tail -= 1


if __name__ == '__main__':
    tests = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([3, 3], 6, [1, 2]),
        ([-5, -4, 4], 0, [2, 3]),
        ([-1, 0], -1, [1, 2]),
    ]
    for nums, target, expected in tests:
        result = Solution().twoSum2(nums, target)
        assert(result == expected)
