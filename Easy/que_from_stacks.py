"""
Implement FIFO queue using only two stacks.
The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Notes:
You must use only standard operations of a stack,
which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively.
You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

Example 1:
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false


Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, peek, and empty.
All the calls to pop and peek are valid.


Follow-up:
Can you implement the queue such that each operation is amortized O(1) time complexity?
In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.


"""


class MyQueue:
    """
    Two stacks:
     1. reverse arrival order of the elements
     2. store the queue elements in their final order
    """

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue
        :param x: int to push at the front of queue
        :return:
        Time: O(N) to traverse through stack1
        Space: O(N) to store stack elements
        """
        while self.stack1:
            s1 = self.stack1.pop()
            self.stack2.append(s1)
        self.stack1.append(x)
        while self.stack2:
            s2 = self.stack2.pop()
            self.stack1.append(s2)

    def pop(self) -> int:
        """
        Removes the element from the front of the queue and returns it.
        :return:
        Time: O(1) Space: O(1)
        """
        return self.stack1.pop()

    def peek(self) -> int:
        """
        :return: Returns the element at the front of the queue.
        Time: O(1) Space: O(1)
        """
        return self.stack1[-1]

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        Stack s1 contains all stack elements, so the algorithm checks s1 size to return if the queue is empty.
        :return: True if empty, false otherwise
        Time: O(1)
        Space: O(1)
        """
        return not self.stack1


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    element_at_peek = obj.peek()
    assert element_at_peek == 1
    obj.pop()
    assert obj.empty() == False
