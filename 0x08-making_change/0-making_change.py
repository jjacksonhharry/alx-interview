#!/usr/bin/python3

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total.

    Args:
        coins (list): A list of integers representing the values
                        of the coins in possession.
        total (int): The target total amount.

    Returns:
        int: The fewest number of coins needed to meet the total.
    """

    # If total is 0 or less, 0 coins are needed
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make change for 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            # Update dp[amount] with the minimum number of coins needed
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Check if the total amount is reachable
    return dp[total] if dp[total] != float('inf') else -1
