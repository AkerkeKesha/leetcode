"""
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
2. Clarifications:
- can ll be empty? If yes, do we consider it is False

3. Edge cases

4. Approach1: have a slow, fast pointers and when fast reaches the end, the slow will be in the middle. In that case,
reverse left half of linked list and check against the right half. Check values of each one by one, then it is palindrome

"""
from basics.linked_list import ListNode, LinkedList
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverse_linked_list(slow)
        fast = head

        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True

    def reverse_linked_list(self, node: ListNode) -> Optional[ListNode]:
        if not node or not node.next:
            return node
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev


if __name__ == '__main__':
    tests = [
        ([1, 2, 2, 1], True),
        ([1, 2], False),
    ]
    for input_list, expected_val in tests:
        input_ll = LinkedList().list2linked_list(input_list)
        result = Solution().isPalindrome(input_ll)
        assert result == expected_val