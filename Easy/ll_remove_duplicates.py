"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.
Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

2. Clarifications
- is the list guaranteed to be sorted? yes
- can input ll be empty? just return empty

3. Edge Cases
- empty linked list

4. Approach1: traverse linked and check neighbouring nodes for equality
Time: O(N)
Space: O(1) for in place changes


"""
from typing import Optional
from basics.linked_list import ListNode, LinkedList


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == '__main__':
    tests = [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([], []),
        ([1], [1])
    ]
    for input_list, output_list in tests:
        input_ll = LinkedList().list2linked_list(input_list)
        result = Solution().deleteDuplicates(input_ll)
        arr = LinkedList().linked_list2list(result)
        assert arr == output_list




