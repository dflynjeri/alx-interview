#!/usr/bin/python3
"""
A module that provides a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Args:
        n (int): The number of rows in Pascal's triangle to generate.
    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    # Return an empty list if n is zero or negative
    if n <= 0:   # Ensure this line has no trailing whitespace
        return []   # This line is indented 4 spaces, which is required
    # Initialize the triangle with the first row
    triangle = [[1]]
    # Generate each row
    for i in range(1, n):
        row = [1]  # Every row starts with 1
        # Calculate the values between the 1's
        for j in range(1, i):
            # Sum of the two numbers above
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)
    return triangle


if __name__ == "__main__":
    print(pascal_triangle(5))
    print(pascal_triangle(1))
    print(pascal_triangle(0))
    print(pascal_triangle(10))
    print(pascal_triangle(100))

# Uncomment the following line to test in command-line if needed
# print(pascal_triangle(5))
