#!/usr/bin/python3
"""
function def island_perimeter(grid): that returns
the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
    - grid (List[List[int]]): A list of lists representing the 2D grid where:
        - 0 represents water
        - 1 represents land

    Returns:
    - int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check the neighbors and subtract 1 for each cell
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
