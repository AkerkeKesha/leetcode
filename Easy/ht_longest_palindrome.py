"""
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.

2. Clarifications:
- can s be empty? no, see constraint

3. Test cases
- case when a letter occurs odd times, e.g. 5 times

4. Approach1:  if letter occurs v times, then v // 2 * 2 partners to build palindrome. At end if there is any v % 2 == 1
then that can be a unique center
Time: O(N) to count each letter and build map
Space: O(1) to store count, O(N) for the map

"""

class Solution:

    def longestPalindrome(self, s: str) -> int:
        letter2count = {}
        result = 0
        for letter in s:
            letter2count[letter] = letter2count.get(letter, 0) + 1
        for val in letter2count.values():
            result += val // 2 * 2  # e.g. for 3 // 2 * 2 = 2, 6 // 2 * 2 = 6
            if result % 2 == 0 and val % 2 == 1:  # after this we switch result to odd, hence no more unique center
                result += 1
        return result


if __name__ == '__main__':
    tests = [
        ("abccccddd", 7),  # dccbccd is one example
        ("abccccdd", 7),  # dccaccd is one example
        ("abccccddddd", 9), #  ddccaccdd
        ("bb", 2),
        ("a", 1),
        ("", 0),


    ]
    for s, expected in tests:
        result = Solution().longestPalindrome(s)
        assert result == expected
