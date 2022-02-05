"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Ex1: Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Ex2: Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

2. Clarifications
can place if flowerbed: ...|0|0|0|... left and right neighbours are zero
3. Edge cases
4. Approach1:  traverse over all the elements of the flowerbed and find out those elements which are 0.
For every such element, we check if its both adjacent positions are also empty. If so, we can plant a flower
at the current position without violating the no-adjacent-flowers-rule.
NOTE: For the first and last elements, we need not check the previous and the next adjacent positions respectively.
Time: O(N) single scan
Space: O(1)

"""
from typing import List


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count_flowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count_flowers += 1
            i += 1
        return count_flowers >= n


if __name__ == '__main__':
    tests = [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 0, 0], 1, True),
        ([1, 0, 0], 1, True),
        ([0, 1, 0], 1, False),
    ]
    for flowerbed, n, expected in tests:
        answer = Solution().canPlaceFlowers(flowerbed, n)
        assert answer == expected
