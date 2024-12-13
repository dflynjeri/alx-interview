#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    """Generate a list of primes up to max_n use the Sieve of Eratosthenes."""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
    return is_prime


def simulate_game(n, is_prime):
    """Simulate a single game and determine the winner."""
    # Create a list to track remaining numbers
    remaining = [True] * (n + 1)
    remaining[0] = remaining[1] = False  # Exclude 0 and 1
    current_turn = 0  # 0 = Maria, 1 = Ben

    while True:
        # Find the first prime still in the set
        move_made = False
        for i in range(2, n + 1):
            if remaining[i] and is_prime[i]:
                # Remove the prime and its multiples
                for j in range(i, n + 1, i):
                    remaining[j] = False
                move_made = True
                break

        if not move_made:
            # No moves left; the current player loses
            return "Ben" if current_turn == 0 else "Maria"

        # Switch turns
        current_turn = 1 - current_turn


def isWinner(x, nums):
    """Determine the overall winner after x rounds."""
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n, is_prime)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
