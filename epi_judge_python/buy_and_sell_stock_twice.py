from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # TODO - you fill in here.
    # profit = 0.0
    #
    # for i in range(len(prices)):
    #     profit_left = buy_and_sell_stock_once(prices[0:i+1])
    #     if i+1 < len(prices):
    #         profit_right = buy_and_sell_stock_once(prices[i+1:])
    #     else:
    #         profit_right = 0.0
    #
    #     profit = max(profit, profit_left + profit_right)
    # return profit
    min_forward = float('inf')
    max_total_profit_forward = 0.0
    profit_forward = [0.0]* len(prices)
    profit_backward = [0.0]*len(prices)

    for i in range(len(prices)):
        min_forward = min(min_forward, prices[i])
        max_total_profit_forward = max(max_total_profit_forward, prices[i] - min_forward)
        profit_forward[i] = max_total_profit_forward

    max_price_so_far = float('-inf')
    max_profit = 0.0
    for i in reversed(range(len(prices) -1)):
        max_price_so_far = max(max_price_so_far, prices[i+1])
        max_profit = max(max_profit, max_price_so_far - prices[i+1])
        profit_backward[i] = max_profit

    #print(profit_forward)
    #print(profit_backward)
    profit = 0.0
    for i in range(len(prices)):
        profit = max(profit, profit_forward[i] + profit_backward[i])

    return profit

def buy_and_sell_stock_once(prices: List[float]) -> float:

    min_value = float('inf')
    profit = 0.0
    #profit_day = [0]*len(prices)
    for ind, price in enumerate(prices):
        min_value = min(min_value, price)
        profit = max(profit, price - min_value)

    return profit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
