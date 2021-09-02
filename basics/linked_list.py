
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"

    def list2linked_list(self, arr: list):
        """
        recursive function to create linked list from a list, where pointers follow the order in input list

        :param arr: some list of values
        :return: None or ListNode
        """
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            return ListNode(arr[0])
        return ListNode(arr[0], next=ListNode().list2linked_list(arr[1:]))


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.head = Node(1)
    second = Node(2)
    linked_list.head.next = second
    third = Node(3)
    second.next = third
    linked_list.print_list()

    ln = ListNode().list2linked_list([1, 0, 2])
    print(ln)


