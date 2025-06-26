#!/usr/bin/python3
"""
Prime Game - Maria and Ben take turns choosing primes and removing
multiples from a set of integers from 1 to n. The player unable to
make a move loses the round.
"""


def isWinner(x, nums):
    """
    Determines the winner of each round of the Prime Game.
    Maria always plays first.

    Args:
        x (int): number of rounds
        nums (list): list of integers for each round

    Returns:
        str or None: name of the player with the most wins, or None if tied
    """

    def count_primes(n):
        """
        Counts the number of prime numbers up to n,
        using the Sieve of Eratosthenes

        Args:
            n (int): upper limit to find primes

        Returns:
            int: count of prime numbers between 1 and n
        """
        if n < 2:
            return 0

        primes = [True for _ in range(n + 1)]
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return sum(primes)

    if not nums or x < 1:
        return None

    maria = 0
    ben = 0

    for n in nums:
        prime_moves = count_primes(n)
        # If odd, Maria wins. If even, Ben wins.
        if prime_moves % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
