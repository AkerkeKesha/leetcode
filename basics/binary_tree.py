from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Node(val=" + str(self.val) + ", left={" + str(self.left) + ", right={" + str(self.right) + "})"


class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def delete_tree(self):
        self.root = None

    def __repr__(self):
        return NotImplementedError

    def _traverse(self, items: List[int], ind: int = 0) -> Optional[TreeNode]:
        """Closure function using recursion bo build tree"""
        if len(items) <= ind or not items[ind]:
            return None

        node = TreeNode(items[ind])
        node.left = self._traverse(items, 2 * ind + 1)
        node.right = self._traverse(items, 2 * ind + 2)
        return node

    def from_list(self, items: List[int]) -> Optional[TreeNode]:
        """

        :param items: the level order, i.e. [3,5,2,1,4,6,7] looks at indices
             0
            / \
           1   2
          /\  /\
        3  4 5  6
        look at indices, left 2i+1 and right 2i+2 for node root i
        :return: tree
        """
        if not items:
            return None

        return self._traverse(items)

    def to_list(self, root: TreeNode) -> List[int]:
        if not root:
            return []


if __name__ == '__main__':
    """
        Create a Tree of structure:
    
              1
             / \
            2   3
          /   \ /  \
       None None None None
   
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(root)

    tr = [1, 2, 3, 4]
    print(Tree().from_list(tr))

    items = [3, 5, 2, 1, 4, 6, 7]
    """
              3
            /  \
           5     2
          /\     /\
        1   4   6  7
       /\   /\ /\  /\
    None None None None None ..
    """
    print(Tree().from_list(items))

    print("---------------------")
    """
    [1, None, 2, 3] 
    means:
       
              1
             / \
           None  2
               /  \
             3    None
    
    """
    # TODO: fix bug when node is None
    tests = [
        ([1, None, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, None, 2], [1, 2]),
    ]
    for items, expected in tests:
        print(Tree().from_list(items))





