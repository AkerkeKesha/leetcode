"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,2]
Output: [1,2]

Example 5:
Input: root = [1,null,2]
Output: [1,2]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

2. Clarifications
- Preorder aka DFs, i.e. use stack for iterative traversal

3. Edge cases

4. Approach1:
Time: O(N)
Space: O(N)

"""
from typing import Optional, List
from basics.binary_tree import TreeNode, Tree


class Solution:

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        if not root:
            return result
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result


if __name__ == '__main__':
    tests = [
        ([1, None, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, 2]),
    ]
    for input_list, expected in tests:
        node = Tree().from_list(input_list)
        result = Solution().preorderTraversal(node)
        # result.tree2list()
        print(result)


