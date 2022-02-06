"""
A binary watch has 4 LEDs on the top which represent the hours (0-11),
and the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

H: 8|4|2|1
M: 32|16|8|4|2|1

H max: 8|x|2|1 = 11 ; 3 LEDs on
M max: 32|16|8|x|2|1 = 59 ; 5 LEDs on

Given an integer turnedOn which represents the number of LEDs that are currently on,
return all possible times the watch could represent. You may return the answer in any order.

Ex1: Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Ex2: Input: turnedOn = 9
Output: []

Constraints:
- The hour must not contain a leading zero. For example, "01:00" is not valid. It should be "1:00".
- The minute must be consist of two digits and may contain a leading zero.
For example, "10:2" is not valid. It should be "10:02".
- 0 <= turnedOn <= 10

2. Clarifications
3. Edge cases
4. Approach1: Count 1's in bit representation of all possible hour and minutes.
Time: O(1) constant num of hours and minutes
Space: O(N) use list to store times

"""
from typing import List


class Solution:

    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour in range(12):
            for mins in range(60):
                if bin(hour).count("1") + bin(mins).count("1") == turnedOn:
                    time = f"{hour}:{mins:02}"
                    result.append(time)
        return result


if __name__ == '__main__':
    tests = [
        (1, ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]),
        (9, []),
    ]
    for turned_on, expected in tests:
        answer = Solution().readBinaryWatch(turned_on)
        assert answer == expected
