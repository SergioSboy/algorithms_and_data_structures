class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(data, 0, 0, self.n - 1)

    def build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self.build(data, 2 * node + 1, start, mid)
            self.build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_range(self, l, r, val, node, start, end):
        if self.lazy[node] != 0:
            self.tree[node] ^= (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] ^= self.lazy[node]
                self.lazy[2 * node + 2] ^= self.lazy[node]
            self.lazy[node] = 0

        if start > end or start > r or end < l:
            return

        if start >= l and end <= r:
            self.tree[node] ^= (end - start + 1) * val
            if start != end:
                self.lazy[2 * node + 1] ^= val
                self.lazy[2 * node + 2] ^= val
            return

        mid = (start + end) // 2
        self.update_range(l, r, val, 2 * node + 1, start, mid)
        self.update_range(l, r, val, 2 * node + 2, mid + 1, end)
        self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query_range(self, l, r, node, start, end):
        if start > end or start > r or end < l:
            return 0

        if self.lazy[node] != 0:
            self.tree[node] ^= (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node + 1] ^= self.lazy[node]
                self.lazy[2 * node + 2] ^= self.lazy[node]
            self.lazy[node] = 0

        if start >= l and end <= r:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query_range(l, r, 2 * node + 1, start, mid)
        right_sum = self.query_range(l, r, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum

    def range_sum(self, l, r):
        return self.query_range(l - 1, r - 1, 0, 0, self.n - 1)

    def range_xor(self, l, r, val):
        self.update_range(l - 1, r - 1, val, 0, 0, self.n - 1)


import sys

input = sys.stdin.read


def main():
    data = input().split()
    n = int(data[0])
    array = list(map(int, data[1:n + 1]))
    q = int(data[n + 1])
    queries = data[n + 2:]

    seg_tree = SegmentTree(array)
    index = 0
    results = []

    while index < len(queries):
        t = int(queries[index])
        l = int(queries[index + 1])
        r = int(queries[index + 2])

        if t == 1:
            results.append(seg_tree.range_sum(l, r))
            index += 3
        elif t == 2:
            x = int(queries[index + 3])
            seg_tree.range_xor(l, r, x)
            index += 4

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
