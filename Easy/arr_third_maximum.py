"""
Given integer array nums, return the third maximum number in this array.
 If the third maximum does not exist, return the maximum number.
Ex 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.

Ex 2:
Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist,
so the maximum (2) is returned instead.

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Can you find an O(n) solution?

Clarification:
1. Could num in nums be negative? Yes, see constraints 2
2. How big is the length? 104
3. Are duplicates possible? Yes, see ex 3
4. Empty input? No, see constraint 1
5. Second maximum, do I care?

Test Cases:
 - edges
 nums = [ -231, 230, 230, 0]
 output: -231
 First max is 0, then 230, third is -231

Approach 1:
Create set from nums to avoid duplicates. Then:
if len < 3 return max
else sort the list (made from the set) in reverse order (descending), sorting is in-place
return the num at index 2.
Time: O(NlogN)
Space: O(N)

Approach 2:
Traverse num and find max value
Traverse second time and find the max value not equal to one you already have
Traverse the last time and return the max value not equal to two values that you have
Time: O(N)
Space: O(1)

"""
from typing import Dict, List


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        """

        :params: nums, -231 <= nums[i] <= 231 - 1
        :rtype: int
        """
        unique_nums = list(set(nums))
        if len(unique_nums) < 3:
            return max(unique_nums)
        else:
            unique_nums.sort(reverse=True)
            return unique_nums[2]

    def get_third_max_num(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        if len(unique_nums) < 3:
            return max(unique_nums)
        max_values = set()
        max_first = max(set(nums))
        max_values.add(max_first)

        second_max = -232
        for num in nums:
            if num > second_max:
                if num not in max_values:
                    second_max = num
        max_values.add(second_max)

        third_max = -232
        for num in nums:
            if num > third_max:
                if num not in max_values:
                    third_max = num
        max_values.add(third_max)
        return third_max


if __name__ == '__main__':

    tests = [
        ([2, 2, 3, 1], 1),
        ([3, 2, 1], 1),
        ([-231, 230, 230, 0], -231),
        ([1, 2], 2),
        ([1, 1, 2], 2)

    ]
    for test, expected in tests:
        result = Solution().thirdMax(nums=test)
        assert result == expected
    print("Finished approach 1")
    for test, expected in tests:
        result = Solution().get_third_max_num(nums=test)
        assert result == expected
    print("Finished approach 2")


