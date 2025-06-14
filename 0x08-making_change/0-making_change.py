#!/usr/bin/python3

""" makeChange function"""


def makeChange(coins, total):
    """ if the the total is zero or less then no coins are needed"""
    if total <= 0:
        return 0

    """ if the list of coins is empty, it is impossible to make change"""
    if not coins:
        return -1

    """ Create a list to store the minimum coins needed for each amount"""
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # No coins needed to make 0

    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] + 1 < min_coins[amount]:
                min_coins[amount] = min_coins[amount - coin] + 1

    return min_coins[total] if min_coins[total] != float('inf') else -1
