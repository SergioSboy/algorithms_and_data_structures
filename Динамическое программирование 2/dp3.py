from collections import deque


def main():
    n, k = map(int, input().split())
    get_coins = list(map(int, input().split()))
    max_coins, num_jumps, restored_path = grasshopper_coins(n, k, get_coins)
    print(max_coins)
    print(num_jumps)
    print(" ".join(map(str, restored_path)))


def grasshopper_coins(n, k, coins_available):
    dp = [0] * (n + 1)
    dp[1] = 0
    queue = deque()
    queue.append(1)
    previous = [-1] * (n + 1)

    for i in range(2, n + 1):
        while queue and queue[0] < i - k:
            queue.popleft()

        dp[i] = dp[queue[0]] + (coins_available[i - 2] if i != n else 0)
        previous[i] = queue[0]

        while queue and dp[i] >= dp[queue[-1]]:
            queue.pop()

        queue.append(i)

    restore_path = []
    current = n
    while current != -1:
        restore_path.append(current)
        current = previous[current]

    restore_path.reverse()
    return dp[n], len(restore_path) - 1, restore_path


main()
