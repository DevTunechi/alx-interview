#!/usr/bin/python3

def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    # Find the maximum n in nums to know up to where we should calculate primes
    max_n = max(nums)

    # Use Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False

    primes = [i for i, is_prime in enumerate(sieve) if is_prime]

    # Determine the winner for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        moves = 0
        # Count how many prime picks can be made
        used = [False] * (n + 1)
        for p in primes:
            if p > n:
                break
            if not used[p]:
                moves += 1
                for multiple in range(p, n + 1, p):
                    used[multiple] = True

        # Determine the winner based on the number of moves
        if moves % 2 == 1:
            # Odd number of moves means Maria wins
            maria_wins += 1
        else:
            # Even number of moves means Ben wins
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
