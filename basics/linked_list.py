from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"


class LinkedList:

    def __init__(self):
        self.head = None

    def from_list(self, arr: list) -> Optional[ListNode]:
        """
        recursive function to create linked list from a list, where pointers follow the order in input list

        :param arr: some list of values
        :return: None or ListNode
        """
        if not arr:
            return None
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=LinkedList().from_list(arr[1:]))

    def to_list(self, head: ListNode) -> Optional[List[int]]:
        result = []
        if not head:
            return result
        while head:
            result.append(head.val)
            head = head.next
        return result

    def search(self, head: ListNode, x: int):
        while head:
            if head.val == x:
                return head
            head = head.next
        return None


if __name__ == '__main__':
    linked_list = LinkedList()
    ln = linked_list.from_list([1, 0, 2])
    print(ln)

    arr = linked_list.to_list(ln)
    print(arr)

    res = linked_list.search(ln, 0)
    print(res)

