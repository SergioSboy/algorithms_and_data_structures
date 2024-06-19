import sys
a = []


def query(x):
    print(x)

    sys.stdout.flush()
    return


n = int(input())
l, r = 0, n + 1

while r - l > 1:
    mid = (l + r) // 2
    query(mid)

    response = input()

    if response == '<':
        r = mid
    else:
        l = mid


if r - l == 1:
    print('!', l)
