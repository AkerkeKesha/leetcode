"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class.

Example 1:
Input
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
Output
[null, null, null, true, false, null, true, null, false]

Explanation
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // return True
myHashSet.contains(3); // return False, (not found)
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // return True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // return False, (already removed)


Constraints:

0 <= key <= 106
At most 104 calls will be made to add, remove, and contains.

"""


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_set = {}

    def add(self, key: int) -> None:
        """
        Inserts the value key into the HashSet.
        :param key: int
        :return: None
        """
        self.hash_set[key] = None

    def remove(self, key: int) -> None:
        """
        Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
        :param key:
        :return:
        """
        if key in self.hash_set:
            del self.hash_set[key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.hash_set


if __name__ == '__main__':
    # Your MyHashSet object will be instantiated and called as such:
    obj = MyHashSet()
    obj.add(key=1)
    obj.remove(key=1)
    result = obj.contains(key=1)
    assert not result
    myHashSet = MyHashSet()
    myHashSet.add(1)  # set = [1]
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(1)  # return True
    assert not myHashSet.contains(3)  # return False, (not found)
    myHashSet.add(2)  # set = [1, 2]
    assert myHashSet.contains(2)  # return True
    myHashSet.remove(2)  # set = [1]
    assert not myHashSet.contains(2)  # return False, (already removed)

