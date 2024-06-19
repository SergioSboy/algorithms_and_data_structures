def hoare_sort_test(a, n):
    for i in range(n):
        a[i], a[i // 2] = a[i // 2], a[i]
    return a

n = int(input())
a = list(range(1, n + 1))
a = hoare_sort_test(a, n)
print(*a)
