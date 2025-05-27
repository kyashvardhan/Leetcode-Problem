def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Update min_price if we find a new lower one
        if price < min_price:
            min_price = price
        # Otherwise calculate potential profit
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)

    return max_profit
