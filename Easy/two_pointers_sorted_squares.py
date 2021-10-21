"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1: Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2: Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?

2. Clarifications
3. Edge cases
4. Approach1: Use two pointers from two ends that stop when they meet. Insert into output array
greater value squared when comparing absolute value
Time: O(N) to iterate through nums
Space: O(N) for array aux.space

"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left, right = 0, n - 1
        while left <= right:
            num_left, num_right = abs(nums[left]), abs(nums[right])
            if num_left > num_right:
                answer[right - left] = num_left ** 2
                left += 1
            else:
                answer[right - left] = num_right ** 2
                right -= 1
        return answer


if __name__ == '__main__':
    tests = [
        ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
        ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
    ]
    for nums, expected in tests:
        result = Solution().sortedSquares(nums)
        assert result == expected