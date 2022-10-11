# Quick Find UnionFind Class


class QuickFind:

    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]

    def find(self, x) -> int:
        """
        O(1) to return root index
        :param x:
        :return:
        """
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        """
        Make the root of y be the root of x
        O(N) to make changes
        :param x:
        :param y:
        :return:
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x: int, y: int) -> bool:
        """
        O(1) to check whether root vertices are equal
        :param x:
        :param y:
        :return:
        """
        return self.find(x) == self.find(y)


class UnionFind:

    def __init__(self, size: int) -> None:
        self.root = [i for i in range(size)]

    def find(self, x) -> int:
        """
        O(N) to make changes and root index
        :param x:
        :return:
        """
        while x != self.root[x]:
            x = self.root[x]
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        """
        Make the root of y be the root of x
        O(N) to make changes
        :param x:
        :param y:
        :return:
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX

    def connected(self, x: int, y: int) -> bool:
        """
        O(N) to check whether root vertices are equal
        :param x:
        :param y:
        :return:
        """
        return self.find(x) == self.find(y)


if __name__ == '__main__':
    qf = QuickFind(10)
    # 1-2-5-6-7 3-8-9 4
    qf.union(1, 2)
    qf.union(2, 5)
    qf.union(5, 6)
    qf.union(6, 7)

    qf.union(3, 8)
    qf.union(8, 9)

    assert(qf.connected(1, 5))  # true
    assert(qf.connected(5, 7))  # true
    assert(not qf.connected(4, 9))  # false

    # 1-2-5-6-7 3-8-9-4
    qf.union(9, 4)
    assert(qf.connected(4, 9))  # true

    # Test Case
    uf = UnionFind(10)
    # 1-2-5-6-7 3-8-9 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    assert(uf.connected(1, 5))  # true
    assert(uf.connected(5, 7))  # true
    assert(not uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    assert(uf.connected(4, 9))  # true

