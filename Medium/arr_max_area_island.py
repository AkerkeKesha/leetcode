"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
Ex 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
 Given the above grid, return 6

Ex 2:
Input: grid = [[1]]
Output: 1

Ex 3:
Input: grid = [[1,0]]
Output: 1

Ex 4:
Input: [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
The length of each dimension in the given grid does not exceed 50.
row == grid.length
col == grid[i].length
1 <= row, col <= 50
grid[i][j] is 0 or 1.

Clarifications
1. Any constraints in terms of space complexity?
2. Any constraints in terms of time?
3. Can I change the array in-place?
4. Can the grid element be None? If so, is max area considered to be 0? What about empty lists in grid?
5. Are the elements in string or integer representation?

Test Cases:
[[1,0]], 1
[[1]], 1
[[]], 0
None, 0
[], 0

Approach1:
Time: O(r*c) traverse each grid cell once
Space: O(r*c)

"""
from typing import List


def check_neighbor(grid, row_idx, col_idx):
    try:
        neighbor = grid[row_idx][col_idx]
        if neighbor == 1:
            return True
    except IndexError:
        return False


def calculate_area(grid, row_idx, col_idx):
    area = 0
    # stack initially filled with the current cell
    stack = [(row_idx, col_idx)]
    while stack:
        r, c = stack.pop()
        if grid[r][c] == 1:
            area += 1
            # reset visited cell to zero
            grid[r][c] = 0
        # check right
        if check_neighbor(grid, r + 1, c):
            stack.append((r + 1, c))
        if check_neighbor(grid, r - 1, c):
            stack.append((r - 1, c))
        if check_neighbor(grid, r, c + 1):
            stack.append((r, c + 1))
        if check_neighbor(grid, r, c - 1):
            stack.append((r, c - 1))
    return area


class Solution:
    @staticmethod
    def maxAreaOfIsland(grid: List[List[int]]) -> int:
        """
        stack: list of squares to visit (stack) in four directions: up, down, right and left
        :param grid:
        :return:
        """
        if not grid:
            return 0
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, calculate_area(grid, i, j))

        return max_area


if __name__ == '__main__':
    test_cases = [
        ([[1]], 1),
        ([[1, 0]], 1),
        ([[]], 0),
        (None, 0),
        ([], 0),
        ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
        ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 7),
        ([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]], 3),
        ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6)

    ]
    for sample_grid, expected_perimeter in test_cases:
        result = Solution.maxAreaOfIsland(sample_grid)
        if result == expected_perimeter:
            continue
        else:
            print(f"failed result {result} != {expected_perimeter}")