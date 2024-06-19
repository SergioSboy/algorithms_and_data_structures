import sys


def insert(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i - 1) // 2]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def extract(heap):
    if len(heap) == 0:
        return None
    min_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    i = 0
    while True:
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        smallest = i
        if left_child < len(heap) and heap[left_child] < heap[smallest]:
            smallest = left_child
        if right_child < len(heap) and heap[right_child] < heap[smallest]:
            smallest = right_child
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return min_val


heap = []
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
for i in range(n):
    insert(heap, A[i])
result = []
for _ in range(n):
    result.append(extract(heap))
print(*result)