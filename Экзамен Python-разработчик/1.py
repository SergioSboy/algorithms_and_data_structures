def max_mark(n, m):
    if n < 7:
        return -1
    else:
        M = -1
        for i in range(n - 6):
            maxim = 0
            flag = False
            for j in range(7):
                if m[i + j] == 2 or m[i + j] == 3:
                    flag = True
                    break
                if m[i + j] == 5:
                    maxim += 1
            if maxim >= M and flag == False:
                M = maxim
    return M


n = int(input())
m = list(map(int, input().split()))
print(max_mark(n, m))
