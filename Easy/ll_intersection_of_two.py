"""
Given the heads of two singly linked-lists headA and headB,
return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Note:
The test cases are generated such that there are no cycles anywhere in the entire linked structure.
Note that the linked lists must retain their original structure after the function returns.

Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'

Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'

Example 3:
Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection


There is custom judge class implemented, but not given to you.

Follow up: Could you write a solution that runs in O(n) time and use only O(1) memory?

Constraints:
The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

2. Clarifications

3. Edge Cases

4. Approach1: Traverse both linked lists, when reached the end switch to other lists' head. Stop when reached the equal
value
Time: O(N)
Space: O(1)
"""
from basics.linked_list import ListNode, LinkedList


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        a_pointer = headA
        b_pointer = headB
        while a_pointer is not b_pointer:
            a_pointer = a_pointer.next if a_pointer else headB
            b_pointer = b_pointer.next if b_pointer else headA
        return a_pointer


if __name__ == '__main__':
    tests = [
        ([4,1,8,4,5], [5,6,1,8,4,5], [8,4,5]),
        ([1,9,1,2,4], [3,2,4], [2,4]),
        # ([2,6,4], [1,5], []),
    ]
    for list_a, list_b, inter_list in tests:
        ll_a = LinkedList().from_list(list_a)
        ll_b = LinkedList().from_list(list_b)
        intersection_head = Solution().getIntersectionNode(ll_a, ll_b)
        print(intersection_head)
        result_list = LinkedList().to_list(intersection_head)
        # assert result_list == inter_list
