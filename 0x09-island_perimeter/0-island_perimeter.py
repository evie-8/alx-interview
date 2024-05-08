#!/usr/bin/python3
"""
Perimeter of an island
"""


def island_perimeter(grid):
    """
    Returns the perimeter
    """
    length = len(grid)
    breath = len(grid[0])
    perimeter = 0
    for x in range(length):
        for y in range(breath):
            if grid[x][y] == 1:
                perimeter += 4
                if (y < breath - 1 and grid[x][y + 1] == 1):
                    perimeter -= 2
                if (x < length - 1 and grid[x + 1][y] == 1):
                    perimeter -= 2
    return perimeter
