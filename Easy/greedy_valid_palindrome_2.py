"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it

Ex1: Input: s = "aba"
Output: true

Ex2: Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Ex3: Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.

2. Clarifications
3. Edge cases
4. Approach1: use two-pointer one from start, the other from the end. Whenever there is a mismatch, check if left or
right substring is a valid palindrome. Return true is that is the case
Time: O(N^2)
Space: O(1)

"""


class Solution:

    def _is_palindrome(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                left_side = s[start:end]
                right_side = s[start+1:end+1]
                return self._is_palindrome(right_side) or self._is_palindrome(left_side)
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    tests = [
        ("aba", True),
        ("abca", True),
        ("abc", False),
        ("abcba", True),
    ]
    for string, expected in tests:
        answer = Solution().validPalindrome(string)
        assert answer == expected
