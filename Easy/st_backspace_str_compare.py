"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a##c", t = "#a#c"
Output: true
Explanation: Both s and t become "c".

Example 4:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".


Constraints:
1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.

Follow up: Can you solve it in O(n) time and O(1) space?

2. Clarifications:

3. Edge Cases

4.
Approach1: For each string if char is backspace, then pop stack, otherwise push char into stack. Compare two stacks
return if are the same
Time: O(N) to iterate over strings
Space: O(N) to store the stack

Approach2: as follow up,
Time:
Space


"""
from typing import List

BACKSPACE = '#'


class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = self.get_stack_from_str(s)
        t_stack = self.get_stack_from_str(t)
        return s_stack == t_stack

    def get_stack_from_str(self, s):
        stack = []
        for char in s:
            if char == BACKSPACE:
                try:
                    stack.pop()
                except IndexError:
                    stack = []
            else:
                stack.append(char)
        return stack


if __name__ == '__main__':
    tests = [
        ("ab#c",  "ad#c", True),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ]
    for s, t, expected in tests:
        result = Solution().backspaceCompare(s, t)
        assert result == expected

