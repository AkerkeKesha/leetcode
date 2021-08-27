"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?


"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Instead of creating two alphabets try to counter[letter] -1 for matching in t
        :param s:
        :param t:
        :return:
        """
        alphabet1 = self.build_alphabet(s)
        alphabet2 = self.build_alphabet(t)
        return alphabet1 == alphabet2

    def build_alphabet(self, s):
        """
        Try cleaner version
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        :param s:
        :return:
        """
        alphabet = {}
        for letter in s:
            if letter in alphabet:
                alphabet[letter] += 1
            else:
                alphabet[letter] = 1
        return alphabet


if __name__ == '__main__':
    tests = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("akerke" ,"ekreka", True),
        ("aka", "kaaa", False),
    ]

    for s, t, expected in tests:
        result = Solution().isAnagram(s, t)
        assert result == expected
