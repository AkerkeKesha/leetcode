"""
Write a function that reverses a string. The input string is given as an array of characters s.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 105
s[i] is a printable ascii character.

2. Clarifications
3. Test cases
4. Approach 1: For reversing a string, we use the opposite directional two-pointer approach
Time: O(n)
Space: O(1)

"""
from typing import List


class Solution:

    def __init__(self):
        self.string = None

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head, tail = 0, len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
        self.string = s


if __name__ == '__main__':
    tests = [
        (["h","e","l","l","o"], ["o","l","l","e","h"]),
        (["H","a","n","n","a","h"], ["h","a","n","n","a","H"]),
    ]
    for input, reversed_str in tests:
        solution = Solution()
        solution.reverseString(input)
        assert(solution.string == reversed_str)
