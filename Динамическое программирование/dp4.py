def get_knight_move(n, m):
    F = [[0] * (m + 3) for _ in range(n + 3)]

    F[2][2] = 1
    starti, startj = 2, 2
    while starti < n + 1 or startj < m + 1:
        if startj == m + 1:
            starti += 1
        else:
            startj += 1

        i, j = starti, startj
        while i <= n + 1 and j >= 2:
            F[i][j] = F[i + 1][j - 2] + F[i - 1][j - 2] + F[i - 2][j - 1] + F[i - 2][j + 1]
            i += 1
            j -= 1
    return F[n + 1][m + 1]


n, m = map(int, input().split())
print(get_knight_move(n, m))