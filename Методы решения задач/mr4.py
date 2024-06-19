def solve(n, k):
    def count(x):
        count = 0
        for r in range(1, n + 1):
            count += min(n, x // r)
        return count >= k

    low, high = 1, n ** 2
    while low < high:
        mid = (low + high) // 2
        if count(mid):
            high = mid
        else:
            low = mid + 1
    return low


n, k = map(int, input().split())
print(solve(n, k))


