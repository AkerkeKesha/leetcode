"""
You are given row x col grid representing a map where
grid[i][j] = 1 represents land and
grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally).
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Ex 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Ex 2:
Input: grid = [[1]]
Output: 4

Ex 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.


Clarifications:
1. Any constraints in terms of time/space complexity?
2. Can grid be None? If so, is perimeter considered to be 0? What about empty lists
3. Are the elements in string or integer representation

Test Cases: edge cases
        [[]]
        None
        []


Approach 1:
Time: O(r * c) row and columns of grid i.e squared
Space: O(1) just store variable and return it

"""
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter


if __name__ == '__main__':
    test_cases = [
        ([[1]], 4),
        ([[1, 0]], 4),
        ([[]], 0),
        (None, 0),
        ([], 0),
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16)

    ]
    for sample_grid, expected_perimeter in test_cases:
        result = Solution().islandPerimeter(sample_grid)
        if result == expected_perimeter:
            continue
        else:
            print(f"failed result {result} != {expected_perimeter}")