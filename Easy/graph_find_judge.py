"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
- The town judge trusts nobody.
- Everybody (except for the town judge) trusts the town judge.
- There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person
 labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Ex1: Input: n = 2, trust = [[1,2]]
Output: 2

Ex2: Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Ex3: Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

2. Clarifications

3. Edge cases

4. Approach1: Observe for judge node we should have in-degree - out-degree = (N-1) + 0, i.e. (N-1) trust from other
vertices and 0 out. Therefore, create a map to count this difference. Return vertex no. that satisfies this. Otherwise,
return -1
Time: O(N)
Space: O(N)

"""
from typing import List


class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree_diff_map = {}
        for person in range(1, n+1):
            degree_diff_map[person] = degree_diff_map.get(person, 0)
        for i in range(len(trust)):
            edges = trust[i]
            # trust[i] = [ai, bi]: a trusts b. in(b) += 1, out(a) += 1, in(a) - out(a) = 0 - 1, in(b) - out(b) = 1 - 0
            first, second = edges[0], edges[1]
            degree_diff_map[first] -= 1
            degree_diff_map[second] += 1
        for person in range(1, n+1):
            if degree_diff_map[person] == (n - 1):
                return person
        return -1


if __name__ == '__main__':
    tests = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
    ]
    for n, trust, expected in tests:
        ans = Solution().findJudge(n, trust)
        assert ans == expected
