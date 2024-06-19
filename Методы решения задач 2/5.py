
s = input().strip()
n = len(s)
packed = [[''] * n for _ in range(n)]

for length in range(1, n + 1):
    for left in range(n - length + 1):
        right = left + length - 1
        minimum = s[left:right + 1]
        if length > 4:
            for right1 in range(left, right):
                left2 = right1 + 1
                temp = packed[left][right1] + packed[left2][right]
                if len(temp) < len(minimum):
                    minimum = temp
            for p in range(1, length):
                if length % p == 0:
                    is_periodic = True
                    for i in range(left + p, right + 1):
                        if s[i] != s[i - p]:
                            is_periodic = False
                            break
                    if is_periodic:
                        temp = str(length // p) + '(' + packed[left][left + p - 1] + ')'
                        if len(temp) < len(minimum):
                            minimum = temp
        packed[left][right] = minimum

print(packed[0][n - 1])
