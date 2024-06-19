def max_white_mushrooms(n, forest):
    dp = [[0] * 3 for _ in range(n)]
    if forest[0] == ['W', 'W', 'W']:
        return 0

    for j in range(3):
        if forest[n - 1][j] == 'C':
            dp[n - 1][j] = 1

    for i in range(n - 2, -1, -1):
        for j in range(3):
            if forest[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i + 1][max(j - 1, 0)], dp[i + 1][j], dp[i + 1][min(j + 1, 2)])
                if forest[i][j] == 'C':
                    dp[i][j] += 1

    max_mushrooms = max(dp[0])

    return max_mushrooms


n = int(input())
forest = []
for _ in range(n):
    s = input()
    l = []
    for i in s:
        l.append(i)
    forest.append(l)

print(max_white_mushrooms(n, forest))
