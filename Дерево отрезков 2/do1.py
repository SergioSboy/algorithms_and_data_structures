import sys
import math

class Segtree:
    def __init__(self, n):
        self.t = [0] * (2 * n)
        self.d = [0] * (2 * n)

    def print_tree(self):
        print(" ".join(map(str, self.t)))
        print(" ".join(map(str, self.d)))

    def change(self, l, r, v, x, xl, xr):
        if l >= xr or xl >= r:
            return
        if xl >= l and xr <= r:
            self.d[x] += v
            self.t[x] += v
            return
        self.propagate(x)
        xm = (xl + xr) // 2
        self.change(l, r, v, 2 * x + 1, xl, xm)
        self.change(l, r, v, 2 * x + 2, xm, xr)
        self.t[x] = min(self.t[2 * x + 1], self.t[2 * x + 2])

    def calc(self, l, r, x, xl, xr):
        if l >= xr or xl >= r:
            return sys.maxsize
        if xl >= l and xr <= r:
            return self.t[x]
        self.propagate(x)
        xm = (xl + xr) // 2
        s1 = self.calc(l, r, 2 * x + 1, xl, xm)
        s2 = self.calc(l, r, 2 * x + 2, xm, xr)
        return min(s1, s2)

    def propagate(self, x):
        self.t[2 * x + 1] += self.d[x]
        self.d[2 * x + 1] += self.d[x]
        self.t[2 * x + 2] += self.d[x]
        self.d[2 * x + 2] += self.d[x]
        self.d[x] = 0


def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    n = 2 ** math.ceil(math.log2(n))
    tree = Segtree(n)
    for _ in range(m):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l, r, v = query[1:]
            tree.change(l, r, v, 0, 0, n)
        else:
            l, r = query[1:]
            print(tree.calc(l, r, 0, 0, n))


if __name__ == "__main__":
    main()