# demonstration of Best Time to Buy and Sell Stock problem solution
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy
# one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# Example:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5 Explanation: Buy on day 2 (price = 1)

# Implementation technique- Two pointers and Sliding window


def maxProfit(prices):
    # left is for buy
    left = 0
    # right is for sell
    right = left + 1
    max_profit = 0
    while right < len(prices):
        if prices[left] < prices[right]:
            max_profit = max(max_profit, prices[right] - prices[left])

        else:
            # move the left pointer to the lowest price
            left = right
        right += 1
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Maximum Profit: ", maxProfit(prices))
