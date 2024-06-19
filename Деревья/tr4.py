import sys


def insert(heap, x):
    heap.append(x)
    i = len(heap) - 1
    while i > 0 and heap[i] > heap[(i-1)//2]:
        heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        i = (i-1) // 2

def extract(heap):
    if len(heap) == 0:
        return None
    max_val = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    i = 0
    while True:
        left_child = 2*i + 1
        right_child = 2*i + 2
        largest = i
        if left_child < len(heap) and heap[left_child] > heap[largest]:
            largest = left_child
        if right_child < len(heap) and heap[right_child] > heap[largest]:
            largest = right_child
        if largest == i:
            break
        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest
    return max_val

heap = []
for _ in range(int(sys.stdin.readline())):
    op, *v = sys.stdin.readline().split()
    op = int(op)
    if op == 0:
        insert(heap, int(v[0]))
    else:
        result = extract(heap)
        print(result)


def extract(A):
    if len(A) < 1:
        return None
    max_val = A[0]
    A[0] = A[-1]
    del A[-1]
    heapify(A, 0, len(A) - 1)
    return max_val


def heapify(A, i, heap_size):
    left = 2 * i
    right = 2 * i + 1
    largest = i
    if left <= heap_size and A[left] > A[largest]:
        largest = left
    if right <= heap_size and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest, heap_size)


A = []
for _ in range(int(sys.stdin.readline())):
    op, *v = sys.stdin.readline().split()
    op = int(op)
    if op == 0:
        insert(A, int(v[0]))
    else:
        print(extract(A))
