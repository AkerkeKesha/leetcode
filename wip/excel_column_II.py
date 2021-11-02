class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        alphabet = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        for char in s:
            print(char)
        return result


if __name__ == '__main__':
    input = 'AB'
    solution = Solution()
    result = solution.titleToNumber(input)
    print(f'{result}')