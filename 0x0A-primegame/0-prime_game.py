#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of primes up to max_n use the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


def calculate_prime_moves(prime_list, max_n):
    """Precompute the number of moves for each n based on prime removals."""
    moves = [0] * (max_n + 1)
    for prime in prime_list:
        for multiple in range(prime, max_n + 1, prime):
            moves[multiple] += 1
    return moves


def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_moves = calculate_prime_moves(primes, max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_moves[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
