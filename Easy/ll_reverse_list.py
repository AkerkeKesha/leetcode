"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

2. Clarifications:
- can ll be empty/None? Yes, see e.g. but should it be None or empty list
- can it have duplicate values? Yes

3. Edge cases

4. Approach1: Iteratively
Time:
Space:

"""
from basics.linked_list import ListNode, linked_list2list
from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

    def reverse_list_recursive(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        if not head:
            return prev
        temp = head.next
        head.next = prev
        return self.reverse_list_recursive(temp, head)  # reverse node excluding me


if __name__ == '__main__':
    tests = [
        ([], None),
        (None, None),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ]
    for input_list, expected_list in tests:
        ll = ListNode().list2linked_list(input_list)
        ll_out = Solution().reverseList(ll)
        res = linked_list2list(ll_out)
        assert res == expected_list
    print("works iteratively")
    for input_list, expected_list in tests:
        ll = ListNode().list2linked_list(input_list)
        ll_out = Solution().reverse_list_recursive(ll)
        res = linked_list2list(ll_out)
        print(input_list)
        assert res == expected_list
    print("works recursively")
