# demonstration of Best Time to Buy and Sell Stock problem solution
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# Example:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# Implementation: simple technique using min and max builtin functions


def maxProfit(prices):
    minPrice = prices[0]
    maxProfit = 0
    for price in prices[1:]:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, (price - minPrice))
    return maxProfit


if __name__ == "__main__":
    prices = [7, 1, 0, 5, 3, 6, 4]
    print("Maximum Profit: ", maxProfit(prices))
