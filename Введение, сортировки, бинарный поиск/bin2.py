def find_closest(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return arr[mid]
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    if right < 0:
        return arr[left]
    elif left >= len(arr):
        return arr[right]

    if abs(arr[left] - x) < abs(arr[right] - x):
        return arr[left]
    elif abs(arr[left] - x) == abs(arr[right] - x):
        return min(arr[left], arr[right])
    else:
        return arr[right]


n, k = map(int, input().split())
arr = list(map(int, input().split()))
queries = list(map(int, input().split()))

for query in queries:
    closest = find_closest(arr, query)
    print(closest)
'''
5 5
1 3 5 7 9
2 4 8 1 6
'''
