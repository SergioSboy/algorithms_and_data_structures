n = int(input())
arr = []
idx = [0] * (n + 1)
tree = [0] * (n + 1)
a = list(map(int, input().split()))
for i in range(1, n + 1):
    arr.append([a[i - 1], i])

def get(i):
    ans = 0
    while i:
        ans += tree[i]
        i -= i & -i
    return ans


def up(i):
    while i <= n:
        tree[i] += 1
        i += i & -i



arr.sort(reverse=True)

for i in range(1, n + 1):
    idx[arr[i - 1][1]] = i

ans = 0
for i in range(1, n + 1):
    temp = get(idx[i])
    ans += temp * (n - i - idx[i] + temp + 1)
    up(idx[i])

print(ans)
