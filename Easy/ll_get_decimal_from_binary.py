"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5

Example 2:
Input: head = [0]
Output: 0

Example 3:
Input: head = [1]
Output: 1

Example 4:
Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880

Example 5:
Input: head = [0,0]
Output: 0

Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

2. Clarifications:
- can linked list be empty? No, see constraints
- How large can linked list be? Max. 30

3. Test cases

4. Approach 1: Traverse the linked list and store all values in a string or array.
convert the values obtained to decimal value in a classic way

Time: O(N) to traverse
Space: O(1) aux space to store num variable

Approach 2: Traverse the linked list and store all values in a string or array.
convert the values obtained to decimal value in using bitwise operation. i.e. num = (num << 1) | x bitwise left shift,
then bitwise OR

Time: O(N) to traverse
Space: O(1) aux space to store num variable

"""
from basics.linked_list import LinkedList, ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        # traverse non-empty Listnode
        while head.next:
            # convert arithmetic way num = num * 2 + x
            num = num * 2 + head.next.val
            head = head.next
        return num

    def get_decimal_value_bitwise(self, head: ListNode) -> int:
        num = head.val
        # traverse non-empty Listnode
        while head.next:
            # convert arithmetic way num = (num << 1) | x
            num = (num << 1) | head.next.val
            head = head.next
        return num


if __name__ == '__main__':
    tests = [
        ([1, 0, 1], 5),
        ([0], 0),
        ([1], 1),
        ([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0], 18880),
        ([0,0], 0),
    ]
    for input_list, expected in tests:
        ln = LinkedList().from_list(input_list)
        ans = Solution().getDecimalValue(ln)
        assert ans == expected
    print("Approach 1 worked")
    for input_list, expected in tests:
        ln = LinkedList().from_list(input_list)
        ans = Solution().get_decimal_value_bitwise(ln)
        assert ans == expected
    print("Approach 2 worked")
