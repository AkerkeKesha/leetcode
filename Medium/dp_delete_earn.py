from typing import List


class Solution:

    def deleteAndEarn(self, nums: List[int]) -> int:
        points = {}
        max_number = 0
        # Precompute how many points we gain from taking an element
        for num in nums:
            points[num] = points.get(num, 0) + num
            max_number = max(max_number, num)

        def max_points(num: int) -> int:
            if num == 0:
                return 0
            if num == 1:
                return points.get(1, 0)
            if num not in memo:
                memo[num] = max(max_points(num - 1), max_points(num - 2) + points.get(num, 0))
            return memo[num]

        memo = {}
        return max_points(max_number)


if __name__ == '__main__':
    tests = [
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
        ([3, 1], 4)
    ]

    for nums, expected in tests:
        result = Solution().deleteAndEarn(nums)
        assert result == expected
