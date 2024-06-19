n = int(input())
k = list(map(int, input().split()))
d = []
p = []
i = 1
m=0
while i < n+1:
    j=0
    jj=0
    while k[j] != i:
        d.append(k[j])
        j += 1
    d.append(k[j])
    p.append([1,j+1])
    del k[:j+1]
    if d[::-1] == sorted(d):
        j = 1
        kk = d.pop()
        if len(d) != 0:
            while kk +1 == d[-1] :
                j += 1
                kk = d.pop()
                if len(d) == 0:
                    break
                if kk == n:
                    break
        p.append([2,j])
    else:
        print(0)
        m=1
        i = n
    i += j
if m != 1:
    print(len(p))
    for i in range(len(p)):
        print(*p[i])
'''
4
4 1 3 2
'''
