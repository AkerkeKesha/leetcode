"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
 to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1: Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2: Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

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
