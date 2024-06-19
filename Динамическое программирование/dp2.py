n = int(input())
a = [[0] * 3 for _ in range(20)]

a[0][0] = a[0][1] = a[0][2] = 1

for i in range(1, n):
    a[i][0] = a[i - 1][1] + a[i - 1][2]
    a[i][2] = a[i][1] = a[i - 1][0] + a[i - 1][1] + a[i - 1][2]

s = sum(a[n - 1])
print(s)