import math


def resize(arr):
    s = len(arr)
    new_s = int(2 ** math.ceil(math.log2(s)))
    while s < new_s:
        s += 1
        arr.append(0)


class Tree:
    def __init__(self, arr):
        self.size = len(arr)
        self.t = [0] * (2 * self.size)
        self.build(arr, 0, 0, self.size)

    def set(self, i, v, x, lx, rx):
        if rx - lx == 1:
            self.t[x] = v
            return
        m = (lx + rx) // 2
        if i < m:
            self.set(i, v, 2 * x + 1, lx, m)
        else:
            self.set(i, v, 2 * x + 2, m, rx)
        self.t[x] = max(self.t[2 * x + 1], self.t[2 * x + 2])

    def above(self, v, l, x, lx, rx):
        if self.t[x] < v:
            return -1
        if rx <= l:
            return -1
        if rx == lx + 1:
            return lx
        m = (lx + rx) // 2
        res = self.above(v, l, 2 * x + 1, lx, m)
        if res == -1:
            res = self.above(v, l, 2 * x + 2, m, rx)
        return res

    def build(self, a, x, lx, rx):
        if rx - lx == 1:
            if lx < len(a):
                self.t[x] = a[lx]
        else:
            m = (lx + rx) // 2
            self.build(a, 2 * x + 1, lx, m)
            self.build(a, 2 * x + 2, m, rx)
            self.t[x] = max(self.t[2 * x + 1], self.t[2 * x + 2])


def main():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    resize(arr)
    n = len(arr)
    t = Tree(arr)
    for _ in range(m):
        v, a, b = map(int, input().split())
        if v == 1:
            t.set(a, b, 0, 0, n)
        else:
            print(t.above(a, b, 0, 0, n))


if __name__ == "__main__":
    main()
