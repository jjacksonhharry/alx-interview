#!/usr/bin/python3
"""
Function that Returns the fewest number of
coins needed to meet total
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet
    a given amount total.

    Args:
    coins (list): A list of the values of the coins in your possession.
    total (int): The total amount to be achieved with the
                 fewest number of coins.

    Returns:
    int: The fewest number of coins needed to meet the total.
         If the total is 0 or less, returns 0.
         If the total cannot be met by any number of coins, returns -1.
    """

    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
