"""
There is an undirected star graph consisting of n nodes labeled from 1 to n.
A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node
 with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between
the nodes ui and vi. Return the center of the given star graph.

Ex1: Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Ex2: Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1

Constraints:
3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph. (i.e. guaranteed to have a star)

2. Clarifications:
Hint: The center is also connected to all other node

3. Edge cases:

4. Approach1: Since center is connected to all other nodes. We can focus on first 2 edges, and explore first 4 vertices.
Time: O(1)
Space: O(1)

"""
from typing import List


class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        first, second = edges[0][0], edges[0][1]
        if first == edges[1][0] or first == edges[1][1]:
            return first
        return second


if __name__ == '__main__':
    tests = [
        ([[1, 2], [2, 3], [4, 2]], 2),
        ([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
    ]
    for edges, expected in tests:
        assert expected == Solution().findCenter(edges)
