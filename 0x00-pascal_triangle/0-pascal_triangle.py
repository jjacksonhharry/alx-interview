#!/usr/bin/python3
"""
function that returns a list of lists of integers
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n(int): The number of rows to generate in Pascal's triangle
    Returns:
        list of lists: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        new = [1] + [prev[j-1] + prev[j] for j in range(1, i)] + [1]
        triangle.append(new)

    return triangle
