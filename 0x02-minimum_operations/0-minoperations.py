#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
        Calcs fewest ops num needed to result in n H chars
    """
    if n <= 1:
        return 0

    ops = 0
    factorizer = 2

    while n > 1:
        if n % factorizer == 0:
            ops += factorizer
            n //= factorizer
        else:
            factorizer += 1

    return ops
