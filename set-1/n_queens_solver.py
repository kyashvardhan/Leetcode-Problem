def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diagonals and (row + col) not in anti_diagonals

    def backtrack(row):
        if row == n:
            board = [''.join(r) for r in chessboard]
            results.append(board)
            return

        for col in range(n):
            if is_safe(row, col):
                chessboard[row][col] = 'Q'
                cols.add(col)
                diagonals.add(row - col)
                anti_diagonals.add(row + col)

                backtrack(row + 1)

                chessboard[row][col] = '.'
                cols.remove(col)
                diagonals.remove(row - col)
                anti_diagonals.remove(row + col)

    results = []
    chessboard = [['.'] * n for _ in range(n)]
    cols = set()
    diagonals = set()
    anti_diagonals = set()

    backtrack(0)
    return results
