#!/usr/bin/python3

def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    max_n = max(nums)

    # Step 1: Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False

    # Step 2: Create a DP table to store the number of prime moves for each n
    dp = [0] * (max_n + 1)

    # Step 3: Compute the number of primes removed (move count) for each n
    for i in range(2, max_n + 1):
        if sieve[i]:
            # For each prime i, simulate removing all multiples of i
            for j in range(i, max_n + 1, i):
                dp[j] += 1

    # Step 4: Determine who wins each game by counting moves
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # If dp[n] is odd, Ben wins; if even, Maria wins
        if dp[n] % 2 == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
