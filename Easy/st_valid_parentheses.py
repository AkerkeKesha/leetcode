"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']'
, determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

2. Clarifications
- If empty string as input, is it True?

3. Edge cases
- consider if you have a single size input
- if use dictionaries, what if KeyError

4. Approach1: Use stack, if opening brackets then push, of closing then check top of stack, if pair of brackets match
then you can pop, and check until the stack becomes empty
Time: O(N) to iterate string
Space: O(N) to use stack as list


"""
from typing import List


class Solution:
    def top(self, stack: List[str]) -> str:
        return stack[len(stack) - 1] if len(stack) > 0 else ''

    def isValid(self, s: str) -> bool:
        bracket_pairs = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        stack = []
        for char in s:
            if char in bracket_pairs:
                stack.append(char)
            else:
                bracket_key = self.top(stack)
                if bracket_key and bracket_pairs[bracket_key] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0


if __name__ == '__main__':
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("]", False),
    ]
    for input, expected in tests:
        result = Solution().isValid(input)
        assert expected == result