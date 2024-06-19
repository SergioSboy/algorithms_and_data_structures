import random
import sys


class TNode:
    gen = random.Random()

    def __init__(self, k):
        self.key = k
        self.prior = TNode.gen.randint(0, 2 ** 32)
        self.left = None
        self.right = None


class TTreap:
    def __init__(self):
        self.Head = None

    def free(self, ptr):
        if ptr is None:
            return
        self.free(ptr.left)
        self.free(ptr.right)
        del ptr

    def split(self, ptr, val):
        if ptr is None:
            return (None, None)
        elif val > ptr.key:
            l, r = self.split(ptr.right, val)
            ptr.right = l
            return (ptr, r)
        else:
            l, r = self.split(ptr.left, val)
            ptr.left = r
            return (l, ptr)

    def merge(self, t1, t2):
        if t1 is None or t2 is None:
            return t2 if t1 is None else t1
        elif t1.prior > t2.prior:
            t1.right = self.merge(t1.right, t2)
            return t1
        t2.left = self.merge(t1, t2.left)
        return t2

    def find_min(self, ptr):
        if ptr is None:
            return -1
        elif ptr.left is None:
            return ptr.key
        return self.find_min(ptr.left)

    def find(self, value):
        l, r = self.split(self.Head, value)
        ans = self.find_min(r)
        self.Head = self.merge(l, r)
        return ans

    def insert(self, value):
        l, r = self.split(self.Head, value)
        self.Head = self.merge(self.merge(l, TNode(value)), r)

    def __del__(self):
        self.free(self.Head)


tree = TTreap()
prev = 0
for i in range(int(sys.stdin.readline())):
    op, v = sys.stdin.readline().split()
    v = int(v)
    if op == '+':
        tree.insert((v + prev) % 1000000000)
        prev = 0
    elif op == '?':
        prev = tree.find(v)
        print(prev)
    else:
        break
