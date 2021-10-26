"""
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50

2. Clarification:
- can ll be empty/none? Yes, see e.g.

3. Edge Cases

4. Approach1: Traverse list and compare values, if equals than set next listnode pointer
Time: O(N)
Space: O(1)
Approach2: Recursively
Time:
Space:
"""
from basics.linked_list import ListNode, LinkedList
from typing import Optional


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy_head = cur = ListNode()
        cur.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next

    def remove_elements(self, head, val):
        if not head:
            return None
        if head.val == val:
            head = self.removeElements(head.next, val)
        else:
            head.next = self.removeElements(head.next, val)
        return head


if __name__ == '__main__':
    tests = [
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([], 1, []),
        ([7, 7, 7, 7], 7, []),
    ]

    for input_list, val, expected_list in tests:
        input_ll = LinkedList().from_list(input_list)
        result = Solution().removeElements(input_ll, val)
        output_ll = LinkedList().to_list(result)
        assert expected_list == output_ll
    print(" -- iterative approach ended successfully ---")
    for input_list, val, expected_list in tests:
        input_ll = LinkedList().from_list(input_list)
        result = Solution().remove_elements(input_ll, val)
        output_ll = LinkedList().to_list(result)
        assert expected_list == output_ll
    print(" -- recursive approach ended successfully ---")


