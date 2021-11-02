"""
Given: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Examples:
Input: s = "III"
Output: 3

Input: s = "IV"
Output: 4

Input: s = "IX"
Output: 9

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:
1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]

Clarifications:
1. Is empty string assumed to ignore?


Test Cases:


Approach: move backwards on the string and map the char with the integer, if the integer is less than or equal prev
running total, then add new value to the result, otherwise subtract (would be either -1, -10, -100)
Time: O(N)
Space: O(1)

"""


class Solution:

    def romanToInt(self, s: str) -> int:
        """

        :return:

        Time: O(N)
        Space: O(1)
        """
        roman_symbols = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        running_total, prev_value = 0, 0
        for i in range(len(s)-1, -1, -1):
            current_char = s[i]
            int_value = roman_symbols[current_char]
            if int_value >= prev_value:
                running_total += int_value
            else:
                running_total -= int_value
            prev_value = int_value

        return running_total


if __name__ == "__main__":
    test_cases = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994)
    ]
    for input, expected_result in test_cases:
        result = Solution().romanToInt(input)
        assert result == expected_result
