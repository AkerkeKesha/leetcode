"""
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians.
That is, all the 1's will appear to the left of all the 0's in each row. E.g. [1, 1, ..., 0, 0]

A row i is weaker than a row j if one of the following is true:
The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.


Example 1: Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3] Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2: Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2] Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].


Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

Approach1: Use binary search to count soldiers
Time: O(nlogm)
Space: O(N) to store the resulting pair

"""
from typing import List


class Solution:
    def get_num_soldiers(self, arr):
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == 1:  # search left side
                left = mid + 1
            else:
                right = mid
        return left

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pairs = []
        for row, arr in enumerate(mat):
            soldiers = self.get_num_soldiers(arr)
            pairs.append((row, soldiers))
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        return [row for row, _ in sorted_pairs][:k]


if __name__ == '__main__':
    tests = [
        ([[1, 1, 0, 0, 0],  # 1, left = 2
          [1, 1, 1, 1, 0],  # 3, left = 4
          [1, 0, 0, 0, 0],  # 0, left = 1
          [1, 1, 0, 0, 0],
          [1, 1, 1, 1, 1]], 3, [2, 0, 3]),
        ([[1, 0, 0, 0],
           [1, 1, 1, 1],
           [1, 0, 0, 0],
           [1, 0, 0, 0]], 2, [0, 2]),
    ]
    for mat, k, expected in tests:
        result = Solution().kWeakestRows(mat, k)
        print(result)

