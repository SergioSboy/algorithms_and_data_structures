import math
import sys

class Node:
    def __init__(self):
        self.real = 0
        self.assignment = math.inf
        self.addition = 0


class SegTree:
    def __init__(self, nn):
        self.tree = [Node() for _ in range(2 * nn)]

    def push_set(self, v, lx, rx):
        if self.tree[v].assignment == math.inf:
            return
        self.tree[v].real = (rx - lx) * self.tree[v].assignment
        if rx - lx != 1:
            self.tree[2 * v + 1].assignment = self.tree[2 * v + 2].assignment = self.tree[v].assignment
            self.tree[2 * v + 1].addition = self.tree[2 * v + 2].addition = 0
        self.tree[v].assignment = math.inf

    def push_add(self, v, lx, rx):
        if self.tree[v].addition == 0:
            return
        self.tree[v].real += (rx - lx) * self.tree[v].addition
        if rx - lx != 1:
            self.tree[2 * v + 1].addition += self.tree[v].addition
            self.tree[2 * v + 2].addition += self.tree[v].addition
            m = (lx + rx) // 2
            self.push_set(2 * v + 1, lx, m)
            self.push_set(2 * v + 2, m, rx)
            self.tree[2 * v + 1].assignment = self.tree[2 * v + 2].assignment = math.inf
        self.tree[v].addition = 0

    def update_set(self, l, r, val, v, lx, rx):
        if self.tree[v].addition == 0:
            self.push_set(v, lx, rx)
        else:
            self.push_add(v, lx, rx)
        if l >= rx or r <= lx:
            return
        if lx >= l and rx <= r:
            self.tree[v].assignment = val
            if self.tree[v].addition == 0:
                self.push_set(v, lx, rx)
            else:
                self.push_add(v, lx, rx)
            return
        m = (lx + rx) // 2
        self.update_set(l, r, val, 2 * v + 1, lx, m)
        self.update_set(l, r, val, 2 * v + 2, m, rx)
        self.tree[v] = Node()
        self.tree[v].real = self.tree[2 * v + 1].real + self.tree[2 * v + 2].real

    def update_add(self, l, r, val, v, lx, rx):
        if self.tree[v].addition == 0:
            self.push_set(v, lx, rx)
        else:
            self.push_add(v, lx, rx)
        if l >= rx or r <= lx:
            return
        if lx >= l and rx <= r:
            self.tree[v].addition = val
            if self.tree[v].addition == 0:
                self.push_set(v, lx, rx)
            else:
                self.push_add(v, lx, rx)
            return
        m = (lx + rx) // 2
        self.update_add(l, r, val, 2 * v + 1, lx, m)
        self.update_add(l, r, val, 2 * v + 2, m, rx)
        self.tree[v] = Node()
        self.tree[v].real = self.tree[2 * v + 1].real + self.tree[2 * v + 2].real

    def get(self, l, r, v, lx, rx):
        if self.tree[v].addition == 0:
            self.push_set(v, lx, rx)
        else:
            self.push_add(v, lx, rx)
        if l >= rx or r <= lx:
            return 0
        if lx >= l and rx <= r:
            return self.tree[v].real
        m = (lx + rx) // 2
        left = self.get(l, r, 2 * v + 1, lx, m)
        right = self.get(l, r, 2 * v + 2, m, rx)
        return left + right




input = sys.stdin.readline
n, m = map(int, input().split())
n = 2 ** math.ceil(math.log2(n))
tree = SegTree(n)
for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        l, r, v = query[1:]
        tree.update_set(l, r, v, 0, 0, n)
    elif query[0] == 2:
        l, r, v = query[1:]
        tree.update_add(l, r, v, 0, 0, n)
    else:
        l, r = query[1:]
        print(tree.get(l, r, 0, 0, n))
