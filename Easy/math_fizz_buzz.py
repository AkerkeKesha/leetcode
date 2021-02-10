"""
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Examples:
n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

Clarification:
1. How big is n?
2. Numbers are positive?
3. Numbers are integers?
4. How does the output look like? Is the string joined?

Test Cases:
n = 3 -> [1, 2 "Fizz"]
n = 0 -> []
n = 30


Naive Approach:
Traverse each number in given range:
    if number % 15 then "FizzBuzz"
    elif number % 5 then "Buzz"
    elif number % 3 then "Fizz"
    else str(number) inserted
Time: O(N)
Space: O(1) ? BUG? Should be O(N)

Solution:

"""

from typing import List
import logging


class Solution:

    def fizzBuzz(self, n: int) -> List[str]:
        """

        :param n: int, upper bound on number of integers
        :return: List[str]

        Time complexity: O(n)
        Space complexity: O(N)

        """
        result = []
        for number in range(1, n+1):
            if number % 15 == 0:
                result.append("FizzBuzz")
            elif number % 5 == 0:
                result.append("Buzz")
            elif number % 3 == 0:
                result.append("Fizz")
            else:
                result.append(str(number))
        return result


if __name__ == '__main__':
    result = Solution().fizzBuzz(n=15)
    print(result)

