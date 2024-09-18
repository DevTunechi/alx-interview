#!/usr/bin/python3
""" Using Personalised Approach """


def makeChange(coins, total) -> int:
    """ Determines the fewest number of coins needed
        to meet a given amount total
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)

    bunch_of_coins = 0
    for c in coins:
        if total == 0:
            break
        bunch_of_coins += total // c
        total %= c

    return bunch_of_coins if total == 0 else -1
