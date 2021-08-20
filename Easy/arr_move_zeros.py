"""
1. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

2. Clarifications:
- Handle empty list? Return empty
- How big is the array? How big are elements?

3. Test Cases:
- consider case when no zero, then keep the order

4. Approach 1: Try with allocating space as naive approach, traverse through input, append to list if not zero, at end
fill in zeros upto original len is reached
Time: O(N) to traverse and append
Space: O(N) to store result array

Approach 2: A two-pointer approach could be helpful here.
The idea would be to have one pointer for iterating the array
and another pointer that just works on the non-zero elements of the array.
Time:
Space: O(1) in place modification of input


"""

from typing import List


class Solution:

    def __init__(self):
        self.nums = None

    def move_zeros_naive(self, nums: List[int]) -> None:
        """
        Do by allocating extra space
        """
        n = len(nums)
        result = []
        for num in nums:
            if num != 0:
                result.append(num)
        while len(result) < n:
            result.append(0)
        self.nums = result
        return self.nums

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first, second = 0, 0
        n = len(nums)
        while first < n:
            if nums[first] != 0:
                nums[second] = nums[first]
                second += 1
            first += 1
        while second < n:
            nums[second] = 0
            second += 1
        self.nums = nums


if __name__ == '__main__':
    tests = [
        ([0,1,0,3,12], [1,3,12,0,0]),
        # 0, 1, 2, 3, 4 index 0, yes, then move to len - 1 , modify this index
        ([0], [0]),
        ([], []),
        ([-1, 1, 20, 3, 12], [-1, 1, 20, 3, 12]),
        ([1, 0, 3, 0, 0, 0],[1, 3, 0, 0, 0, 0])
    ]
    for nums, expected in tests:
        sol = Solution()
        sol.move_zeros_naive(nums)
        assert sol.nums == expected
    for nums, expected in tests:
        sol2 = Solution()
        sol2.moveZeroes(nums)
        assert sol2.nums == expected


