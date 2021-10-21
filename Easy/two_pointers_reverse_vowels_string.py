"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

2. Clarifications
3. Edge cases
4. Approach1:
Time: O(n)
Space: O(n) to convert string to list and vice-versa

"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        head, tail = 0, len(s) - 1
        while head < tail:
            if s[head] in vowels and s[tail] in vowels:
                s[head], s[tail] = s[tail], s[head]
            elif s[tail] not in vowels:
                tail -= 1
                continue
            elif s[head] not in vowels:
                head += 1
                continue
            head += 1
            tail -= 1
        return ''.join(s)


if __name__ == '__main__':
    tests = [
        ("hello",  "holle"),
        ("leetcode", "leotcede"),
    ]
    for input, expected in tests:
        result = Solution().reverseVowels(input)
        assert result == expected

