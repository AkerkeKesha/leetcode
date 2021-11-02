class Solution:
    '''
    Time: O(logn)
    Space: O(n)
    '''
    def convertToTitle(self, n: int) -> str:
        result = ''
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while n != 0:
            n -= 1
            r = n % 26
            n = n // 26
            result = alphabet[r] + result
            # print(n,r)
        return result.strip()


if __name__ == '__main__':
    values = [
        (28, "AB"),
        (701, "ZY"),
        (2826, "DDR"),
        (0, "")
    ]

    for value, expected in values:
        solution = Solution()
        result = solution.convertToTitle(value)
        print('Expected: {}, Result: {}'.format(expected, result))
        assert expected == result
