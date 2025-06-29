def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])

    # Update grid in-place with minimum path sums
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue  # Start point
            elif i == 0:
                grid[i][j] += grid[i][j - 1]
            elif j == 0:
                grid[i][j] += grid[i - 1][j]
            else:
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[-1][-1]
