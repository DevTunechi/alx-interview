def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start by adding 4 for the land cell

                # Check the cell above (i-1, j)
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

                # Check the cell to the left (i, j-1)
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

    return perimeter
