"""
Write a function to delete a node in a singly-linked list.
You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
It is guaranteed that the node to be deleted is not a tail node in the list.

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Example 3:
Input: head = [1,2,3,4], node = 3
Output: [1,2,4]

Example 4:
Input: head = [0,1], node = 0
Output: [1]

Example 5:
Input: head = [-3,5,-99], node = -3
Output: [5,-99]

Constraints:

The number of the nodes in the given list is in the range [2, 1000].
-1000 <= Node.val <= 1000
The value of each node in the list is unique. The node to be deleted is in the list and is not a tail node
2. Clarifications:
- duplicates
- exist or not
- could it be tail node
- can ll be empty or None?

3. Edge cases

4. Approach1: We don't have access to head, we can't just traverse and rearrange nodes. Instead
Time:
Space:


"""
from basics.linked_list import ListNode, LinkedList


class Solution:

    def __init__(self, listnode: ListNode=None):
        self.ListNode = listnode

    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next  # node.next will not be null, it is never a tail node


if __name__ == '__main__':
    tests = [
        ([4, 5, 1, 9], 5, [4, 1, 9]),
        ([4, 5, 1, 9], 1, [4, 5, 9]),
        ([1, 2, 3, 4], 3, [1, 2, 4]),
        ([0, 1], 0, [1]),
        ([-3, 5, -99], -3, [5, -99])
    ]
    for input_list, node_val, output_list in tests:
        ll = LinkedList()
        ln = ll.from_list(input_list)
        sl = Solution(ln)
        node = ll.search(ln, node_val)
        sl.deleteNode(node)
        res = ll.to_list(sl.ListNode)
        assert res == output_list

