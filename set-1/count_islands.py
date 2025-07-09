def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()

    def dfs(r, c):
        if (
            r < 0 or c < 0 or
            r >= rows or c >= cols or
            grid[r][c] == '0' or
            (r, c) in visited
        ):
            return
        visited.add((r, c))
        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs(r, c)
                island_count += 1

    return island_count
