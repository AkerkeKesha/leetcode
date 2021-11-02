class Solution:
    '''
    Difference from part 1: You may complete as many transactions as you like
     (i.e., buy one and sell one share of the stock multiple times).
    Time Complexity O(n)
    Space Complexity O(1)
    '''
    def maxProfit(self, prices) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.maxProfit(prices)
    print(f'{result}')
