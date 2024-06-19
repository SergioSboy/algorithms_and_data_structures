def max_coins(n, k, coins):
    dp = [0] * (n + 1)
    prev = [-1] * (n + 1)

    dp[1] = coins[0]
    for i in range(2, n + 1):
        max_val = float('-inf')
        max_j = -1
        for j in range(1, min(i, k) + 1):
            if dp[i - j] + coins[i - 2] > max_val:
                max_val = dp[i - j] + coins[i - 2]
                max_j = i - j
        dp[i] = max_val
        prev[i] = max_j

    max_coins = dp[n]
    jumps = []
    while n != -1:
        jumps.append(n)
        n = prev[n]

    return max_coins, len(jumps), jumps[::-1]


n, k = map(int, input().split())
coins = list(map(int, input().split()))

max_coins, jumps, path = max_coins(n, k, coins)
print(max_coins)
print(jumps)
print(*path)
