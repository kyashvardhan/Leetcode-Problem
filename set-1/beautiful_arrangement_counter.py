def countArrangement(n):
    count = 0
    visited = [False] * (n + 1)

    def backtrack(pos):
        nonlocal count
        if pos > n:
            count += 1
            return
        for i in range(1, n + 1):
            if not visited[i] and (i % pos == 0 or pos % i == 0):
                visited[i] = True
                backtrack(pos + 1)
                visited[i] = False

    backtrack(1)
    return count
