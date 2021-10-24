"""
Find the max sum subarray of fixed size k

"""


def find_max_sum(array, k) -> int:
    current_running_sum = 0
    max_so_far = float('-inf')  # some really small value
    for i in range(len(array)):
        current_running_sum += arr[i]
        if i >= k - 1:  # within window size
            max_so_far = max(max_so_far, current_running_sum)
            current_running_sum -= array[i - (k - 1)]  # subtract furthest right val
    return max_so_far


if __name__ == '__main__':
    tests = [
        ([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 16),
        ([2, 3, 4, 1, 5], 10),
    ]
    for arr, expected in tests:
        result = find_max_sum(arr, k=3)
        assert result == expected
