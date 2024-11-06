#!/usr/bin/python3
"""
Calculates the minimum number of operations to reach exactly `n` H characters.
"""


def minOperations(n):
    """Determines the minimum number of Copy All and Paste operations
    to get exactly `n` H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: Minimum number of operations or 0 if impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # While the divisor divides n, divide n and count the divisor as
        # operations
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
