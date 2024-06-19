n, k = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
min_e = a[0]
max_e = a[n-1]

for i in b:
    if min_e <= i <= max_e:
        mid = n // 2
        r = n - 1
        l = 0
        while a[mid] != i and l <= r:
            if i > a[mid]:
                l = mid + 1
            else:
                r = mid - 1
            mid = (r + l) // 2
        if l > r:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')

'''
10 5
1 2 3 4 5 6 7 8 9 10
-2 0 4 9 12
'''
