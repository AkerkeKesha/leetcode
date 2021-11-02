import sys


class Solution:
    '''
    You are only permitted to complete at most one transaction
    (i.e., buy one and sell one share of the stock)
    Time Complexity: Loop runs n(n-1)/2 times, thus O(n^2)
    Space Complexity: two vars, O(1)
    '''

    def maxProfit(self, prices) -> int:
        max_profit = 0
        no_prices = len(prices)
        for i in range(no_prices):
            for j in range(i+1, no_prices):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

    def max_profit(self, prices):
        '''
        Time complexity: O(n)
        Space complexity: O(1)
        :param prices:
        :return:
        '''
        min_price = sys.maxsize
        max_profit = 0
        no_prices = len(prices)
        for i in range(no_prices):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    result = solution.max_profit(prices)
    print(f'{result}')
