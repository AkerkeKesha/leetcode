"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

Follow up: Could you find an O(n + m) solution? Hint: can we make even better, using binary search
O(nlogm), n = no. of rows, m = no. of cols

2. Clarifications
- Note that grid is sorted both column and row-wise (important for binary search)
- How big can values in array be? Overflow possible? No, not big
3. Edge cases
4. Approach1: Try binary search algo on each row, if negative number is met, increase count, move left otherwise right
Note -> since array is sorted it is enough to get the first index of negative number, then count = length - first index.
Time: O(nlogm)
Space: O(1) aux space to store var

"""
from typing import List


class Solution:

    def search_negative(self, arr) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] < 0:
                right = mid
            else:
                left = mid + 1
        return len(arr) - left

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for arr in grid:
            count += self.search_negative(arr)
        return count


if __name__ == '__main__':
    tests = [
        ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]], 8),
        ([[3, 2], [1, 0]], 0),
        ([[1, -1], [-1, -1]], 3),
    ]
    for grid, expected in tests:
        result = Solution().countNegatives(grid)
        assert result == expected