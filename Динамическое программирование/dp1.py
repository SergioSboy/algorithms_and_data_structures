n = int(input())
N = list(map(int, input().split()))
DP = []
for i in range(n):
    if i == 0:
        DP.append(N[i])
    elif i == 1:
        DP.append(min(N[i] + DP[i - 1], N[i]))
    else:
        DP.append(min(DP[i - 1] + N[i], DP[i - 2] + N[i]))
print(DP[-1])
