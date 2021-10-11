"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1: Input: nums = [4,2,5,7]
Output: [4,5,2,7] Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2: Input: nums = [2,3]
Output: [2,3]

Constraints:
2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000

Follow Up: Could you solve it in-place?

2. Clarifications:
- can numbers be negative? No

3. Edge Cases

4. Approach1: Use two pointers approach, where we start with index 0 for even numbers and with index 1 for odd numbers.
We can have the following options:
if nums[i] % 2 == 0, then number is already on place, so we look at the next place for i. Advance by 2
if nums[j] % 2 == 1, then number is already on place, so we look ate the next place for j. Advance by 2
In the opposite case we need to switch elements.

Time: O(N) to iterate array
Space: O(1) in place operations

"""
from typing import List


class Solution:

    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(nums)
        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    tests = [
        ([4, 2, 5, 7], [4, 5, 2, 7]),
        ([2, 3], [2, 3]),
    ]
    for nums, expected in tests:
        result = Solution().sortArrayByParityII(nums)
        assert expected == result
