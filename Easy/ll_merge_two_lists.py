"""
Merge two sorted linked lists and return it as a sorted list.
 The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

2. Clarifications:

3. Edge Cases

4. Approach1: Create a dummy head, create curr that will always point to the tail of the resulting sorted linked list,
then curr will point to the smallest values between two input linked lists
Time: O(N)
Space: O(1)

Approach2:
Time:
Space:

"""
from typing import Optional
from basics.linked_list import ListNode, LinkedList


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = curr = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy_head.next

    def merge_two_lists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            node = ListNode(l1.val)
            node.next = self.merge_two_lists(l1.next, l2)
        else:
            node = ListNode(l2.val)
            node.next = self.merge_two_lists(l1, l2.next)
        return node


if __name__ == '__main__':
    tests = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]
    for l1, l2, output in tests:
        ll1 = LinkedList().from_list(l1)
        ll2 = LinkedList().from_list(l2)
        result = Solution().mergeTwoLists(ll1, ll2)
        assert output == LinkedList().to_list(result)
    print("--- iterative approach ended successfully ---")
    for l1, l2, output in tests:
        ll1 = LinkedList().from_list(l1)
        ll2 = LinkedList().from_list(l2)
        rec = Solution().merge_two_lists(ll1, ll2)
        assert output == LinkedList().to_list(rec)
    print("--- recursive approach ended successfully ---")
