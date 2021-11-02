"""
Given a signed 32-bit integer x, return x with its digits reversed.
 If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1: Input: x = 123
Output: 321

Example 2: Input: x = -123
Output: -321

Example 3: Input: x = 120
Output: 21

Example 4: Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1

2. Clarifications
3. Edge Cases
4. Approach1:
Time:
Space:

"""


class Solution:

    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        digits = str(abs(x))
        res = int(digits[::-1])
        res = res if x > 0 else -res
        if -2 ** 31 < res < 2 ** 31:
            return res
        return 0


if __name__ == "__main__":
    tests = [
        (123, 321),
        (-123, -321),
        (120, 21),
        (0, 0)
    ]
    for input, expected in tests:
        res = Solution().reverse(input)
        assert expected == res