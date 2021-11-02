"""
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False,
"aab" -> True,
"carerac" -> True.

Hint:
Consider the palindromes of odd vs even length. What difference do you notice?
Count the frequency of each character. If each character occurs even number of times,
then it must be a palindrome. How about character which occurs odd number of times?

2. Clarifications
3. Edge cases
4. Approach1:
Time: O(N) to iterate string
Space: O(N) to store the hashsets
"""


class Solution:

    def palindrome_permutation(self, s: str) -> bool:
        freq = set()
        for char in s:
            if char in freq:
                freq.remove(char)
            else:
                freq.add(char)
        return len(freq) <= 1


if __name__ == '__main__':
    tests = [
        ("code", False),
        ("aab", True),
        ("carerac", True),
        ("accccdddd", True),
    ]
    for string, expected in tests:
        result = Solution().palindrome_permutation(string)
        assert result == expected

