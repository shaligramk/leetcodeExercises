""""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

"""    

def maxProfit(self, prices: List[int]) -> int:
    """
    rtype: int
    """
    if not prices:
        return []

    max_profit = 0
    buy_price = prices[0]

    for price in prices:
        if price < buy_price:
            buy_price = price
        else:
            max_profit = max(max_profit, price - buy_price)

    return max_profit
 