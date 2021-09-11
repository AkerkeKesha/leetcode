"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

2. Clarifications:
- if list if empty? do we return false, no cycle
3. Edge cases:

4. Approach1: Have a slow node and fast node traverse the list, if slow = fast then return cycle true. If fast reached
null then it is the end of list, so return false
Time: O(N)
Space: O(1)

"""
from basics.linked_list import ListNode, LinkedList


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next  # fast = slow would fail the case when [1]
        while fast is not slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


if __name__ == '__main__':
    tests = [
        (),
        (),
    ]