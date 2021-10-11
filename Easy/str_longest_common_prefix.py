"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1: Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2: Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

2. Clarifications
3. Edge cases
4. Approach1:
Time: O(S) where S is sum of all chars in string
Space: O(1)

"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        for index, char in enumerate(shortest):
            for word in strs:
                if word[index] != char:
                    return shortest[:index]
        return shortest


if __name__=="__main__":
    tests = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    ]
    for strs, expected in tests:
        result = Solution().longestCommonPrefix(strs)
        assert result == expected