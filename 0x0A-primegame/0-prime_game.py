#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game over multiple rounds.

    Args:
    x (int): The number of rounds.
    nums (list of int): An array where each element represents
    the maximum number (n) in a round.

    Returns:
    str: The name of the player that won the most rounds.
    If there is a tie, return None.
    """
    if not nums or x <= 0:
        return None

    max_num = max(nums)

    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes.

    for start in range(2, int(max_num ** 0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, max_num + 1, start):
                is_prime[multiple] = False

    # Create a cumulative count of prime numbers up to each index.
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    def play_game(n):
        """
        Determine the winner for a single round of
        the game with maximum number n.

        Args:
        n (int): The maximum number in the current round.

        Returns:
        str: The name of the winner ("Maria" or "Ben").
        """
        if prime_count[n] % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    # Track the number of wins for Maria and Ben.
    maria_wins = 0
    ben_wins = 0

    # Determine the winner for each round.
    for num in nums:
        winner = play_game(num)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner.
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
