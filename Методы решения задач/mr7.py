import sys


def convert_arr_to_intervals(arr):
    if arr[:3] <= arr[3:]:
        return [(
            arr[0] * 3600 + arr[1] * 60 + arr[2],
            arr[3] * 3600 + arr[4] * 60 + arr[5]
        )]
    else:
        return [
            (arr[0] * 3600 + arr[1] * 60 + arr[2], 86400),
            (0, arr[3] * 3600 + arr[4] * 60 + arr[5])
        ]


def t_o(n, intervals):
    events = []
    for interval in intervals:
        for start, end in interval:
            if start == end:
                n -= 1
            else:
                events.append((start, 1))
                events.append((end, -1))
    events.sort()
    total_time = 0
    open_count = 0
    last_time = 0

    for time, change in events:
        if open_count == n:
            total_time += time - last_time
        open_count += change
        last_time = time
    return total_time


n = int(sys.stdin.readline())
intervals = list(
    map(
        convert_arr_to_intervals,
        map(
            lambda x: list(map(int, x)),
            (input().split() for _ in range(n))
        )
    )
)
print(t_o(n, intervals))
