"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.
Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

2. Clarifications:
 - emptry string will result in empty string?

3. Test Cases:

        "1" + "9" = "10" there is still carry
        "0" + "0" = "0"

4. Approach 1: traverse through string reversely, add digits and keep track of carry. Take care when you are done with one
number, don't forget to add 0. If both nums have same length and carry "overflows" dont forget to increase the length!
Time: O(n)
Space:

"""


class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        result, carry, i = [], 0 , 0
        num1, num2 = num1[::-1], num2[::-1]
        len1, len2 = len(num1), len(num2)
        max_length_to_traverse = max(len1, len2)
        while i < max_length_to_traverse or carry:
            digit1 = int(num1[i]) if i < len1 else 0
            digit2 = int(num2[i]) if i < len2 else 0
            sum = (digit1 + digit2 + carry) % 10
            carry = (digit1 + digit2 + carry) // 10
            result.append(str(sum))
            i += 1
        return ''.join(result[::-1])


if __name__ == '__main__':
    tests = [
        ("1", "9", "10"),
        ("11", "123", "134"),
        ("0", "0", "0"),
        ("456", "77", "533"),
        ("", "", ""),
        ("9", "99", "108")
    ]
for num1, num2, expected in tests:
    result = Solution().addStrings(num1, num2)
    assert(result == expected)



