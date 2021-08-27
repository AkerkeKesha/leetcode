"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2, because v is the first unique character and it is at index 2

Example 3:
Input: s = "aabb"
Output: -1, because every character repeats at least once.


Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.

2. Clarifications
- can s be empty? yes, then return -1

3. Test cases
- empty input
- more than 2 appearances of the letter

4. Approach 1: Create char2count map of a string. For each char in s check if it exists in map with value > 1
then return its index
Time: O(N) traverse through array, O(1) map search
Space: O(N) to store the map, O(1) auxiliary

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char2count = {}
        for letter in s:
            char2count[letter] = char2count.get(letter, 0) + 1
        for index, letter in enumerate(s):
            if letter in char2count:
                if char2count[letter] == 1:
                    return index
        return -1


if __name__ == '__main__':
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
    ]
    for s, expected in tests:
        result = Solution().firstUniqChar(s)
        assert result == expected
