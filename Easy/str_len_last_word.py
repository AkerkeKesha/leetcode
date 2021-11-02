"""
Given a string s consisting of some words separated by some number of spaces,
return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1: Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2: Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3: Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

2. Clarifications
3. Edge cases
4. Approach1:
Time: O(N) to iterate the sentence
Space: O(1)

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        n = len(words)
        return len(words[n-1])


if __name__ == "__main__":
    tests = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("s", 1),
        (" a ", 1)
    ]
    for s, expected in tests:
        result = Solution().lengthOfLastWord(s)
        assert result == expected