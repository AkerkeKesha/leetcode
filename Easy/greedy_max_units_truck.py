"""
You are assigned to put some amount of boxes onto one truck.
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.

You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.

Constraints:
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106

Ex1: Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8

Ex2: Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

2. Clarifications
3. Edge cases
4. Approach1: First, sort the box types with the number of units per box non-increasingly.
Iterate on the box types and take from each type as many as you can.
Time: O(NlogN)
Space: O(N)

"""
from typing import List


class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        max_units, cur_size = 0, truckSize
        for num_box, units in boxTypes:
            if cur_size <= 0:
                break
            max_units += min(cur_size, num_box) * units
            cur_size -= min(cur_size, num_box)
        return max_units


if __name__ == '__main__':
    tests = [
        ([[5, 10], [2, 5], [4, 7], [3, 9]], 10, 91),
        ([[1, 3], [2, 2], [3, 1]], 4, 8),
    ]
    for box_types, truck_size, expected in tests:
        answer = Solution().maximumUnits(box_types, truck_size)
        assert answer == expected
