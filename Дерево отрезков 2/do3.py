class Node:
    def __init__(self, left, right):
        self.number = self.segments = 0
        self.set = self.up = False
        self.left = left
        self.right = right

def build(tree, v, tl, tr):
    tree[v] = Node(tl, tr)
    if tl != tr:
        tm = (tl + tr) // 2
        build(tree, v * 2, tl, tm)
        build(tree, v * 2 + 1, tm + 1, tr)

def push(tree, v):
    if not tree[v].up:
        return
    tree[v].number = tree[v].right - tree[v].left + 1 if tree[v].set else 0
    tree[v].segments = 1 if tree[v].set else 0
    tree[v].up = False
    if tree[v].left == tree[v].right:
        return
    tree[v * 2].set = tree[v * 2 + 1].set = tree[v].set
    tree[v * 2].up = tree[v * 2 + 1].up = True

def update(tree, v, value, l, r):
    if tree[v].right < l or tree[v].left > r:
        return
    if tree[v].right <= r and tree[v].left >= l:
        push(tree, v)
        tree[v].set = value
        tree[v].up = True
        return
    push(tree, v)
    update(tree, v * 2, value, l, r)
    update(tree, v * 2 + 1, value, l, r)
    cur = v * 2
    while True:
        push(tree, cur)
        if tree[cur].left == tree[cur].right:
            break
        cur = cur * 2 + 1
    left = tree[cur].number == 1
    cur = v * 2 + 1
    while True:
        push(tree, cur)
        if tree[cur].left == tree[cur].right:
            break
        cur = cur * 2
    right = tree[cur].number == 1
    tree[v].number = tree[v * 2].number + tree[v * 2 + 1].number
    tree[v].segments = tree[v * 2].segments + tree[v * 2 + 1].segments
    if left and right:
        tree[v].segments -= 1

if __name__ == "__main__":
    tree = [Node(0, 0) for _ in range(1000100 * 4)]
    build(tree, 1, 0, 1000100)
    n = int(input())
    for _ in range(n):
        color, x, l = input().split()
        x, l = int(x), int(l)
        if l > 0:
            l -= 1
        else:
            l += 1
        update(tree, 1, color == 'B', x + 500000, x + l + 500000)
        print(tree[1].segments, tree[1].number)
