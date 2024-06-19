def max_white_mushrooms(n, forest):
    dp = [[0] * 3 for _ in range(n)]
    if forest[0] == ['W', 'W', 'W']:
        return 0

    for j in range(3):
        if forest[0][j] == 'C':
            dp[0][j] = 1
    maxim = 0
    for i in range(1, n):
        if forest[i] == ['W', 'W', 'W']:
            return max(dp[i - 1])
        for j in range(3):
            if forest[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i - 1][min(j + 1, 2)], dp[i - 1][j], dp[i - 1][max(j - 1, 0)])
                if forest[i][j] == 'C':
                    dp[i][j] += 1
        maxim = max(max(dp[i]), maxim)

        if (forest[i] == ['.', 'W', 'W'] or forest[i] == ['C', 'W', 'W']) and i !=  n - 2:
            if forest[i + 1] == ['W', 'W', '.'] or forest[i + 1] == ['W', 'W', 'C'] :
                print(forest[i])
                return maxim
        print(forest[i], i, n)
        if (forest[i] == ['W', 'W', '.'] or forest[i] == ['W', 'W', 'C'])  and i != n - 2:
            print(forest[i])
            if forest[i + 1] == ['.', 'W', 'W'] or forest[i + 1] == ['C', 'W', 'W']:

                return maxim
    # Find the maximum value in the first row of dp matrix
    for i in dp:
        print(i)
    max_mushrooms = (max(dp[n - 1]))
    return max_mushrooms


n = int(input())
forest = []
for _ in range(n):
    s = input()
    l = []
    for i in s:
        l.append(i)
    forest.append(l)
# forest = [
#     ['W', '.', 'W'],
#     ['C', 'W', 'C'],
#     ['W', '.', 'W'],
#     ['C', 'W', 'W']
# ]
print(max_white_mushrooms(n, forest))
'''
5
.C.
.WC
C.W
.C.
WWW
'''

'''
5
.C.
CWC
C.W
.C.
WWW
'''

'''
5
.W.
C..
C.C
WWC
CWW
'''