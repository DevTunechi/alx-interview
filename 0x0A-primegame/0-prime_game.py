#!/usr/bin/python3

"""Prime Game"""


def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n.
    """
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):  # Fix here, increment by `p` not `p*2`
                prime[i] = False
        p += 1
    return prime


def count_primes_up_to(prime):
    """Count the number of primes up to each index."""
    return [sum(prime[:i+1]) for i in range(len(prime))]


def isWinner(x, nums):
    """Determines winner of prime game."""
    if x == 0 or not nums:
        return None

    n = max(nums)
    prime = sieve_of_eratosthenes(n)
    prime_count = count_primes_up_to(prime)

    player1 = sum(prime_count[num] & 1 for num in nums)
    return "Maria" if player1 > len(nums) // 2 else "Ben"
