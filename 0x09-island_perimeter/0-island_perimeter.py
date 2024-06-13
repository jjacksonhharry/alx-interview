#!/usr/bin/python3
"""
function that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.

    Args:
        grid (list of list of int): A list of lists where 0
        represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Check all four directions contributing to the perimeter
                # Check Up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check Down
                if r == rows - 1 or grid[r+1][c] == 0:
                    perimeter += 1
                # Check Left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check Right
                if c == cols - 1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
