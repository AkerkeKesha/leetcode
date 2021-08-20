"""
1. Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

2. Clarifications:
- Can numbers be negative? Nope, assume not
- How big are elements? How big is the size? Not huge, size max = 250-500
- Handling empty array? Return empty list

3. Test Cases:

4. Approach 1: Notice we add nums[0], nums[0+n] elements to result at each iteration
Time: O(N) to traverse array even upto middle
Space: O(N) for input and resulting list

"""

from typing import List


class Solution:

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.extend([nums[i], nums[i+n]])
        return result


if __name__ == '__main__':
    tests = [
        ([2,5,1,3,4,7], 3, [2,3,5,4,1,7]),
        ([1,2,3,4,4,3,2,1], 4, [1,4,2,3,3,2,4,1]),
        ([1,1,2,2], 2, [1,2,1,2]),
        [], 0, []
    ]