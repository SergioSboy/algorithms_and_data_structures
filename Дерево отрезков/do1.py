class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build_tree()

    def build_tree(self):
        def build(node, start, end):
            if start == end:
                self.tree[node] = self.arr[start]
            else:
                mid = (start + end) // 2
                left_child = 2 * node
                right_child = 2 * node + 1
                build(left_child, start, mid)
                build(right_child, mid + 1, end)
                self.tree[node] = self.tree[left_child] + self.tree[right_child]

        build(1, 0, self.n - 1)

    def update(self, index, value):
        def update_node(node, start, end):
            if start == end:
                self.arr[index] = value
                self.tree[node] = value
            else:
                mid = (start + end) // 2
                left_child = 2 * node
                right_child = 2 * node + 1
                if start <= index <= mid:
                    update_node(left_child, start, mid)
                else:
                    update_node(right_child, mid + 1, end)
                self.tree[node] = self.tree[left_child] + self.tree[right_child]

        update_node(1, 0, self.n - 1)

    def query(self, left, right):
        def query_range(node, start, end, left, right):
            if start > right or end < left:
                return 0
            if left <= start and end <= right:
                return self.tree[node]
            mid = (start + end) // 2
            left_child = 2 * node
            right_child = 2 * node + 1
            left_sum = query_range(left_child, start, mid, left, right)
            right_sum = query_range(right_child, mid + 1, end, left, right)
            return left_sum + right_sum

        return query_range(1, 0, self.n - 1, left, right)


def main():
    m, n = map(int, input().split())
    arr = list(map(int, input().split()))
    segment_tree = SegmentTree(arr)

    for _ in range(n):
        op = input().split()
        if op[0] == '1':
            i, v = map(int, op[1:])
            segment_tree.update(i, v)
        elif op[0] == '2':
            l, r = map(int, op[1:])
            print(segment_tree.query(l, r - 1))


if __name__ == "__main__":
    main()
