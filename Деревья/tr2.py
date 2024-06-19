import sys

sys.setrecursionlimit(10 ** 9)


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def build_tree(n, root, edges):
    nodes = [Node(i) for i in range(n)]
    root_node = nodes[root]

    for i, (left_child, right_child) in enumerate(edges):
        if left_child != -1:
            nodes[i].left = nodes[left_child]
        if right_child != -1:
            nodes[i].right = nodes[right_child]

    return root_node


n, root = map(int, input().split())
edges = []
for _ in range(n):
    op, v = sys.stdin.readline().split()
    edges.append([int(op), int(v)])
tree_root = build_tree(n, root, edges)


def is_avl(node):
    if not node:
        return True, 0

    left_balanced, left_height = is_avl(node.left)
    right_balanced, right_height = is_avl(node.right)

    balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
    height = max(left_height, right_height) + 1

    return balanced, height


def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True

    if node.key <= min_val or node.key >= max_val:
        return False

    return is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)


avl_tree, _ = is_avl(tree_root)
if avl_tree and is_bst(tree_root):
    print(1)
else:
    print(0)
