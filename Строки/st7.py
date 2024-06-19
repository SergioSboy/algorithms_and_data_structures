import sys
from collections import Counter


def calculate_hash(subsequence):
    counter = Counter(subsequence)
    hash_value = ''.join([f"{element}:{count}|" for element, count in sorted(counter.items())])
    return hash_value


def find_max_length_subsequence(n, sequence1, m, sequence2):
    max_length = 0
    hash_map = {}

    for i in range(n):
        for j in range(i + 1, n + 1):
            hash_value = calculate_hash(sequence1[i:j])
            hash_map[hash_value] = max(hash_map.get(hash_value, 0), j - i)

    for i in range(m):
        for j in range(i + 1, m + 1):
            hash_value = calculate_hash(sequence2[i:j])
            max_length = max(max_length, hash_map.get(hash_value, 0))

    return max_length


n = int(sys.stdin.readline())
sequence1 = list(map(int, sys.stdin.readline().split()))
m = int(input())
sequence2 = list(map(int, sys.stdin.readline().split()))

result = find_max_length_subsequence(n, sequence1, m, sequence2)

print(result)
