import sys


class Point:
    def __init__(self, value, isBegin):
        self.value = value
        self.isBegin = isBegin


def solve():
    global mas
    mas.sort(key=lambda x: (x.value, not x.isBegin))
    totalLen = 0
    segmAmount = 1
    prev = mas[0].value
    for i in range(1, len(mas)):
        if segmAmount != 0:
            totalLen += mas[i].value - prev
        prev = mas[i].value
        if mas[i].isBegin:
            segmAmount += 1
        else:
            segmAmount -= 1
    print(totalLen)


n = int(sys.stdin.readline())
mas = [Point(0, False) for _ in range(2 * n)]
for i in range(0, 2 * n, 2):
    begin, end = map(int, sys.stdin.readline().split())
    mas[i] = Point(begin, True)
    mas[i + 1] = Point(end, False)
solve()
