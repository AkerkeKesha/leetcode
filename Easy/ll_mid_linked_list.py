"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

2. Clarifications:
- can ll be empty?
- can ll be None?
- what if ll is 1 element?

3. Edge cases

4. Approach 1: Put every node into an array A in order.
Then the middle node is just A[A.length // 2], since we can retrieve each node by index.
Time: O(N) to traverse the linked list
Space: O(N) to store into list of linked list

Approach 2: When traversing the list with a pointer slow,
make another pointer fast that traverses twice as fast.
When fast reaches the end of the list, slow must be in the middle.
Time: O(N) to traverse linked list
Space: O(1) to store only vars

"""
from basics.linked_list import ListNode, LinkedList
from typing import Optional
from math import ceil


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Make an array of ListNodes, return list of Listnodes starting from mid node
        :param head:
        :return:
        """
        if not head:
            return None
        result = [head]
        while head.next:
            result.append(head.next)
            head = head.next
        mid = int(ceil(len(result) // 2))
        return result[mid]

    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        # consider case when head is None/empty or we reach end node, then fast.next throws error
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4, 5], [3, 4, 5]),
        ([1, 2, 3, 4, 5, 6], [4, 5, 6]),
        ([1], [1]),
        (None, []),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 7, 8])
    ]
    for input_list, output_list in tests:
        input_ll = LinkedList().list2linked_list(input_list)
        result = Solution().middle_node(input_ll)
        arr = LinkedList().linked_list2list(result)
        assert arr == output_list