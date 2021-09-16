"""
You are given a string s consisting of lowercase English letters.
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"

Example 2:
Input: s = "azxxzy"
Output: "ay"

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.

2. Clarifications:

3. Edge Cases:
- empty string

4. Approach1: go through string and push char into stack, then when exploring next char check against top of stack
pop stack if matches.
"""
from typing import List


class Solution:
    def top(self, stack: List[str]) -> str:
        return stack[len(stack) - 1] if len(stack) > 0 else ""

    def removeDuplicates(self, s: str) -> str:
        stack = []
        for char in s:
            if char == self.top(stack):
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)


if __name__ == '__main__':
    tests = [
        ("abbaca", "ca"),
        ("azxxzy", "ay"),
        ("", ""),
        ("abc", "abc"),
        ("aa", ""),
        ("aaa", "a"),
    ]
    for input, expected in tests:
        result = Solution().removeDuplicates(input)
        assert result == expected