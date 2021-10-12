"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
 you must instead have the result be placed in the first part of the array nums.
 More formally, if there are k elements after removing the duplicates,
 then the first k elements of nums should hold the final result.
 It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1: Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2: Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:
0 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

2. Clarifications:
- can nums be empty?
3. Edge cases
- when nums is empty list
4. Approach1: Have two pointers: one to traverse array, the other to keep track of unique elements.
When values are not same (i.e. duplicated) then unique can advance further and swap values at this point.
Otherwise, just advance current pointer
Time: O(N) to iterate over array with current pointer
Space: O(1) in place swapping, no extra space. Constant pointers

"""
from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        """

        :param nums: array of int, sorted in non-decreasing order
        :return: Return k after placing the final result in the first k slots of nums.
        """
        if not nums:
            return 0
        unique, current = 0, 1
        while current < len(nums):
            if nums[unique] != nums[current]:
                unique += 1
                nums[unique] = nums[current]
            current += 1
        return unique + 1


if __name__ == "__main__":
    tests = [
        ([1, 1, 2], 2, [1, 2, 1]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4, 2, 3, 3, 4]),
        ([], 0, [])
    ]
    for nums, k, expected in tests:
        res = Solution().removeDuplicates(nums)
        assert k == res
        for i in range(k):
            assert nums[i] == expected[i]
