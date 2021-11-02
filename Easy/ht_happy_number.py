"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
1 <= n <= 2^31 - 1

2. Clarifications:
- how big can n get? 2^31 almost
- can n be negative? no, see constraints

3. Test cases:
- case when 1 will appear in the iteration

4. Approach1: 2 parts to design
Given a number n, what is its next number? Use modulus and division to get the next number
Follow a chain of numbers and detect if we've entered a cycle. Use Hashset if we have met the number before.

Time: O(logn) to get the number of digits
Space: O(logn) numbers in the Hash set will be stored

"""

class Solution:

    def isHappy(self, n: int) -> bool:
        # pick the digits one by one
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)  # same as (x // y, x % y)
                total_sum += digit ** 2
            return total_sum
        seen = set()
        while n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1


if __name__ == '__main__':
    tests = [
        (19, True),
        (2, False),
        (1, True),
        (0, False),
        (7, True),
        (116, False),
        (100, True),
        (999, False),

    ]
    for n, expected in tests:
        result = Solution().isHappy(n)
        assert result == expected

