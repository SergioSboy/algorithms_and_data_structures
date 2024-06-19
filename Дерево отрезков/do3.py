class SegmentTree:
    def __init__(self, array):
        self.size = len(array)
        self.tree = [0] * (4 * self.size)
        self.construct_tree(array, 0, 0, self.size - 1)

    def construct_tree(self, array, node, start, end):
        if start == end:
            self.tree[node] = array[start]
        else:
            mid = (start + end) // 2
            self.construct_tree(array, 2 * node + 1, start, mid)
            self.construct_tree(array, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index):
        self._update(0, 0, self.size - 1, index)

    def _update(self, node, start, end, index):
        if start == end:
            self.tree[node] = 1 - self.tree[node]
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self._update(2 * node + 1, start, mid, index)
            else:
                self._update(2 * node + 2, mid + 1, end, index)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, k):
        return self._query(0, 0, self.size - 1, k)

    def _query(self, node, start, end, k):
        if start == end:
            return start
        mid = (start + end) // 2
        if self.tree[2 * node + 1] >= k:
            return self._query(2 * node + 1, start, mid, k)
        else:
            return self._query(2 * node + 2, mid + 1, end, k - self.tree[2 * node + 1])

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
initial_state = list(map(int, input().split()))

segment_tree = SegmentTree(initial_state)

for _ in range(m):
    operation, *args = map(int, input().split())
    if operation == 1:
        segment_tree.update(args[0])
    elif operation == 2:
        print(segment_tree.query(args[0] + 1))
