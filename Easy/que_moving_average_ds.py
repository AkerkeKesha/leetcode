"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

2. Clarifications:
- how many times next() will be called
- how big can size be?
- can val be negative? Yes

3. Edge cases:
- size is zero

4. Approach1: add val to sum and array, if size increases then pop and negate from sum. return average value
Time: O(N) to append, pop
Space: O(N) to store internal array
"""


class MovingAverage:
    def __init__(self, size: int):
        self._size = size
        self._array = []
        self._sum = 0

    def next(self, val: int) -> float:
        self._sum += val
        self._array.append(val)
        if len(self._array) > self._size:
            self._sum -= self._array.pop(0)
        return self._sum/len(self._array)


if __name__ == '__main__':
    expected = [1.0, 5.5, 4.666666666666667, 6.0]
    values = [1, 10, 3, 5]
    mov = MovingAverage(3)
    for ind, num in enumerate(values):
        result = mov.next(num)
        assert result == expected[ind]



