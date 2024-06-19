import sys
class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [None] * (4 * len(arr))
        self.build_tree(0, 0, len(arr) - 1)

    def build_tree(self, node, start, end):
        if start == end:
            self.tree[node] = (self.arr[start], 1)
        else:
            mid = (start + end) // 2
            self.build_tree(2 * node + 1, start, mid)
            self.build_tree(2 * node + 2, mid + 1, end)
            left_min, left_count = self.tree[2 * node + 1]
            right_min, right_count = self.tree[2 * node + 2]
            if left_min < right_min:
                self.tree[node] = (left_min, left_count)
            elif left_min > right_min:
                self.tree[node] = (right_min, right_count)
            else:
                self.tree[node] = (left_min, left_count + right_count)

    def update(self, node, start, end, idx, val):
        if start == end:
            self.arr[idx] = val
            self.tree[node] = (val, 1)
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self.update(2 * node + 1, start, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, end, idx, val)
            left_min, left_count = self.tree[2 * node + 1]
            right_min, right_count = self.tree[2 * node + 2]
            if left_min < right_min:
                self.tree[node] = (left_min, left_count)
            elif left_min > right_min:
                self.tree[node] = (right_min, right_count)
            else:
                self.tree[node] = (left_min, left_count + right_count)

    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return float('inf'), 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        left_min, left_count = self.query(2 * node + 1, start, mid, left, right)
        right_min, right_count = self.query(2 * node + 2, mid + 1, end, left, right)
        if left_min < right_min:
            return left_min, left_count
        elif left_min > right_min:
            return right_min, right_count
        else:
            return left_min, left_count + right_count

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
segment_tree = SegmentTree(arr)

for _ in range(m):
    operation = list(map(int, input().split()))
    if operation[0] == 1:
        segment_tree.update(0, 0, n - 1, operation[1], operation[2])
    elif operation[0] == 2:
        min_value, count_min = segment_tree.query(0, 0, n - 1, operation[1], operation[2] - 1)
        print(min_value, count_min)
