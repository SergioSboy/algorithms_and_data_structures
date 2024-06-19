import heapq

def min_sum_digits_divisible_by_k(K):
    # Initializing heap with (distance, node)
    heap = [(0, 1)]  # Start from node 1 with distance 0
    distances = {1: 0}  # Stores the shortest distance to each node

    while heap:
        dist, node = heapq.heappop(heap)

        # If we reached node 0, return the distance
        if node == 0:
            return dist + 1

        # Adding node + 1 to the heap
        next_node = (node + 1) % K
        if next_node not in distances or dist + 1 < distances[next_node]:
            distances[next_node] = dist + 1
            heapq.heappush(heap, (dist + 1, next_node))

        # Adding node * 10 to the heap
        mult_node = (node * 10) % K
        if mult_node not in distances or dist < distances[mult_node]:
            distances[mult_node] = dist
            heapq.heappush(heap, (dist, mult_node))

    return -1  # If no solution found

# Example usage
K = int(input())
print(min_sum_digits_divisible_by_k(K))