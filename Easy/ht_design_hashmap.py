"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.

void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.

int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Constraints:

0 <= key, value <= 106
At most 104 calls will be made to put, get, and remove.


2. Test cases:
- if key is already in map, just update to new value

3. Clarifications

4. Time:
Space:

"""


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hash_map[key] = value  # if key in self.hash_map, update value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hash_map[key] if key in self.hash_map else -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hash_map:
            del self.hash_map[key]


# Your MyHashMap object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyHashMap()
    obj.put(1, 10)
    obj.put(1, 20)
    param_2 = obj.get(1)
    assert param_2 == 20
    obj.remove(1)

    myHashMap = MyHashMap()
    myHashMap.put(1, 1)  # The map is now[[1, 1]]
    myHashMap.put(2, 2)  # The map is now[[1, 1], [2, 2]]
    res = myHashMap.get(1)     # return 1, The map is now[[1, 1], [2, 2]]
    assert res == 1
    res2 = myHashMap.get(3)     # return -1(i.e., not found), The map is now[[1, 1], [2, 2]]
    assert res2 == -1
    myHashMap.put(2, 1)  # The map is now[[1, 1], [2, 1]](i.e., update the existing value)
    res3 = myHashMap.get(2)     # return 1, The map is now[[1, 1], [2, 1]]
    assert res3 == 1
    myHashMap.remove(2)  # remove the mapping for 2, The map is now[[1, 1]]
    res4 = myHashMap.get(2)     # return -1(i.e., not found), The map is now[[1, 1]]
    assert res4 == -1





