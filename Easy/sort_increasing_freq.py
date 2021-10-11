"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
 If multiple values have the same frequency, sort them in decreasing order.
Return the sorted array.


Example 1: Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:
Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:
Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]


Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100

2. Clarifications
3. Edge Cases
4. Approach1:
Time:
Space:

"""
from typing import List


class Solution:

    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        # 1. sort key, val pairs according to values in ascending order
        # 2. when tie values, sort keys in descending order
        pairs = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        result = []
        for key, val in pairs:
            result.extend([key] * val)
        return result


if __name__ == '__main__':
    tests = [
        ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
        ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
        ([-1, 1, -6, 4, 5, -6, 1, 4, 1], [5, -1, 4, 4, -6, -6, 1, 1, 1]),
    ]
    for nums, expected in tests:
        result = Solution().frequencySort(nums)
        assert result == expected
