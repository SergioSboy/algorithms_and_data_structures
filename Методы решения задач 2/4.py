L, N = map(int, input().split())
cuts = [0] + list(map(int, input().split())) + [L]
dp = [[0] * (N + 2) for _ in range(N + 2)]
for i in range(N + 1, -1, -1):
    for j in range(i + 1, N + 2):
        if j - i == 1:
            dp[i][j] = 0
            continue
        dp[i][j] = float('inf')
        for k in range(i + 1, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

print(dp[0][N + 1])


