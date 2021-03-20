"""
Given two arrays, write a function to compute their intersection.
Each element in the result must be unique. The result can be in any order.

Ex1:
 Given nums1 = [1, 2, 2, 1], nums2 = [2, 2],
 return [2].


Constraints:
Duplicates are possible

Clarifications:
1. Any constraints in terms of time/space complexity
2. Can numbers be negative?
3. Are there any constraints in terms of length?
4. How are large are arrays?
5. Can we expect empty arrays? Then do we return empty result?
6. Is there significant difference between nums1 and nums2 in terms of size?

Test Cases:
1. nums1 = [] , nums2 = [1, 2, 3] return []
2. nums1 = [-1, 0, 0, 9], nums2 = [3, 4] return []

Approach 1: first convert both lists to set and return intersection of them as list
Time: O(n)
Space: O(n)
"""

from typing import List


class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        if not nums2:
            return []
        return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    test_cases = [
        ([1, 2, 2, 1], [2, 2], [2]),
        ([], [2, 2], []),
        ([2, 2], [], []),
        ([-1, 0, 0, 9], [3, 4], []),
        ([1, 2, 3, 2, 1], [2, 2, 3], [2, 3]),

    ]
    for nums1, nums2, expected_result in test_cases:
        actual_result = Solution().intersection(nums1, nums2)
        assert len(actual_result) == len(expected_result) and sorted(actual_result) == sorted(expected_result)