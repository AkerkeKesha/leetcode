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
from abc import ABC
from typing import List


class Solution(ABC):
    def reverseString(self, s: List[str]) -> List[str]:
        pass


class IterativeSolution(Solution):
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        head, tail = 0, len(s) - 1
        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1
        return s


class RecursiveSolution(Solution):
    def reverseString(self, s: List[str]) -> List[str]:
        """
        Do not return anything, modify s in-place instead.
        """
        return self._reverse_recursively(s=s, start=0, end=len(s) - 1)

    def _reverse_recursively(self, s: List[str], start, end) -> List[str]:
        if start >= end:
            return s
        s[start], s[end] = s[end], s[start]
        return self._reverse_recursively(s, start + 1, end - 1)


def test(solution: Solution, input_value: List[str], expected: List[str]):
    actual = solution.reverseString(input_value)
    assert (actual == expected)


if __name__ == '__main__':
    tests = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]
    for input_value, expected in tests:
        test(solution=IterativeSolution(), input_value=input_value.copy(), expected=expected)
        test(solution=RecursiveSolution(), input_value=input_value.copy(), expected=expected)
