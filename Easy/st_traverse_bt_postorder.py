"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Post order means post left-right-root
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [2,1]

Example 5:
Input: root = [1,null,2]
Output: [2,1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

2. Clarifications
- Post order, aka BFS, left-right-root

3. Edge cases:
- one root element only

4. Approach1:
Time:
Space:

"""
from basics.binary_tree import TreeNode, Tree
from typing import Optional, List


class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Stack contains have (node, not/visited) tuple
        :param root: TreeNode structure, could be None
        :return:
        """
        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return result


if __name__ == '__main__':
    tests = [
        ([1, None, 2, 3], [3, 2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, None, 2], [2, 1]),
    ]
    for input_list, expected in tests:
        node = Tree().from_list(input_list)
        result = Solution().postorderTraversal(node)
        print(result)
        # assert result == expected
