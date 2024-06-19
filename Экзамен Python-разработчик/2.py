n, m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

rotated = tuple(zip(*A[::-1]))


for i in rotated:
    print(*i)




