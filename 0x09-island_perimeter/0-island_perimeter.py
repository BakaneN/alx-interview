#!/usr/bin/python3
"""Calculate the perimeter of an island from a 2D grid"""


def island_perimeter(grid):
    """Returns the total perimeter of land surrounded by water"""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0] if rows > 0 else 0
            
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1
            """check left"""
            if col == 0 or grid[row][col - 1] == 0:
                perimeter += 1
            """check right"""
            if col == cols -1 or grid[row][col + 1] == 0:
                perimeter += 1
            """check up"""
            if row == 0 or grid[row - 1][col] == 0:
                perimeter += 1
            """check down"""
            if row == rows - 1 or grid[row + 1][col] == 0:
                perimeter += 1
    return perimeter
