#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Expected: 4

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))  # Expected: 7

