"""
1. You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels.

Letters are case sensitive.

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.

2. Clarifications:
- can jewels and/or stones be empty? return zero
- what if letter in jewels that is missing in stones?
- all jewels are unique, so no need to build a set
3. Test Cases:


4. Approach1: Create a dict based on counters
Time: O(N) to traverse strings
Space: O(N) to store dict, O(1) auxiliary space

"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        jewelry = set(jewels)
        for s in stones:
            result += 1 if s in jewelry else 0
        return result


if __name__ == '__main__':
    tests = [
        ("aA", "aAAbbbb", 3),
        ("z", "ZZ", 0),
        ("", "abc", 0),
        ("z", "aAz", 1),
        ("z", "aAb", 0),
    ]
    for jewels, stones, expected in tests:
        result = Solution().numJewelsInStones(jewels, stones)
        assert result == expected
