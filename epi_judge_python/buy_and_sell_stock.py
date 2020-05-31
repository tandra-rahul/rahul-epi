from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    if len(prices) <= 1:
        return 0.0

    profit = 0.0
    cumsum = 0.0

    for i in range(1, len(prices)):
        cumsum = max(0, cumsum + prices[i] - prices[i-1])
        profit = max(profit, cumsum)

    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
