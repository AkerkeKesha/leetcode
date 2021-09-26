"""

Example 1:
Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
Output: 0

Example 2:
Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
Output: 3

Constraints:
1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.

2. Clarifications
- can sandwiches or students be empty? Nope, according to constraints
3. Edge cases
4. Approach1: Just simulate the given. Pop both sandwiches and students, then reset curr index to 0 if preference matches,
otherwise advance curr and append the front of queue to the end. Continue until the end is reached
Time: O(N) to iterate, to re-arrange arrays after pop
Space: O(N) to store inputs

"""
from typing import List


class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        curr = 0
        while students:
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(0)
                curr = 0
            else:
                front = students.pop(0)
                students.append(front)
                curr += 1
            if curr >= len(students):
                break
        return len(students)


if __name__ == '__main__':
    tests = [
        ([1, 1, 0, 0], [0, 1, 0, 1], 0),
        ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
    ]
    for students, sandwiches, expected in tests:
        result = Solution().countStudents(students, sandwiches)
        assert result == expected
