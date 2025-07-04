def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == '1':
                dp[i][j] = min(
                    dp[i - 1][j],     # top
                    dp[i][j - 1],     # left
                    dp[i - 1][j - 1]  # top-left
                ) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side
