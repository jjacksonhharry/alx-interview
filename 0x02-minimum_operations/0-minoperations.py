#!/usr/bin/python3
"""
calculates the fewest number of operations needed to
result in exactly n H characters in the file
"""

from math import log2


def minOperations(n):
    """
    Calculate the minimum number of operations to obtain
    exactly n 'H' characters.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 0:
        return 0

    dp = [float('inf')] * (n + 1)

    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0
