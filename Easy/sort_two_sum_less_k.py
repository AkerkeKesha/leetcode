"""
Given an array A of integers and integer K, return the maximum S such that
there exists i < j with A[i] + A[j] = S and S < K.
If no i, j exist satisfying this equation, return -1.

Example 1:
Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
[1, 8, 23, 24, 33, 34, 54, 75]

Example 2:
Input: A = [10,20,30], K = 15
Output: -1
Explanation: In this case it's not possible to get a pair sum less that 15.

Note:
1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000

2. Clarification
- can numbers be negative? No
- can numbers be empty? No

3. Edge Cases

4. Approach1: First sort the array, then use two pointers technique from two ends.
If two pairs pointed by pointers are less than or equal to target, then move the tail pointer towards middle
Otherwise advance the head pointer
Time: O(NlogN) to sort
Space: O(NlogN) or O(N) depending on the type of sorting algorithm

"""
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        # N logN
        nums.sort()
        # two pointers
        head = 0
        tail = len(nums) - 1
        max_sum = -1
        while head < tail:
            if nums[head] + nums[tail] >= k:
                tail -= 1
            else:
                max_sum = max(max_sum, nums[head] + nums[tail])
                head += 1
        return max_sum


if __name__ == '__main__':
    tests = [
        ([34, 23, 1, 24, 75, 33, 54, 8], 60, 58),
        ([10, 20, 30], 15, -1),
    ]
    for nums, target, expected in tests:
        result = Solution().twoSumLessThanK(nums, target)
        assert result == expected
