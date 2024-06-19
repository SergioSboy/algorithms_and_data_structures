import sys
class SegmentTree:
    def __init__(self, dist):
        self.n = len(dist)
        self.mn = [0] * (4 * self.n)
        self.mn_len = [0] * (4 * self.n)
        self.add = [0] * (4 * self.n)
        self.build(1, 0, self.n, dist)

    def build(self, v, l, r, dist):
        if l + 1 == r:
            self.mn_len[v] = dist[l]
        else:
            m = (l + r) // 2
            self.build(2 * v, l, m, dist)
            self.build(2 * v + 1, m, r, dist)
            self.mn_len[v] = self.mn_len[2 * v] + self.mn_len[2 * v + 1]

    def push(self, v):
        self.add[2 * v] += self.add[v]
        self.mn[2 * v] += self.add[v]
        self.add[2 * v + 1] += self.add[v]
        self.mn[2 * v + 1] += self.add[v]
        self.add[v] = 0

    def update(self, v, l, r, lx, rx, val):
        if r <= lx or rx <= l:
            return
        if lx <= l and r <= rx:
            self.add[v] += val
            self.mn[v] += val
            return

        self.push(v)
        m = (l + r) // 2
        self.update(2 * v, l, m, lx, rx, val)
        self.update(2 * v + 1, m, r, lx, rx, val)

        if self.mn[2 * v] == self.mn[2 * v + 1]:
            self.mn[v] = self.mn[2 * v]
            self.mn_len[v] = self.mn_len[2 * v] + self.mn_len[2 * v + 1]
        elif self.mn[2 * v] < self.mn[2 * v + 1]:
            self.mn[v] = self.mn[2 * v]
            self.mn_len[v] = self.mn_len[2 * v]
        else:
            self.mn[v] = self.mn[2 * v + 1]
            self.mn_len[v] = self.mn_len[2 * v + 1]

    def update_range(self, lx, rx, val):
        self.update(1, 0, self.n, lx, rx, val)

    def query(self):
        return 0 if self.mn[1] else self.mn_len[1]


class Event:
    def __init__(self, x, y1, y2, event_type):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.type = event_type


def main():
    input = sys.stdin.readline
    n = int(input())

    events = []
    yyy = set()

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        if x1 > x2 or y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        x2 += 1
        y2 += 1
        yyy.add(y1)
        yyy.add(y2)
        events.append(Event(x1, y1, y2, 1))
        events.append(Event(x2, y1, y2, -1))
    events.sort(key=lambda e: (e.x, -e.type))

    sorted_yyy = sorted(yyy)
    y_coord_index = {y: i for i, y in enumerate(sorted_yyy)}

    dist = [sorted_yyy[i] - sorted_yyy[i - 1] for i in range(1, len(sorted_yyy))]
    sum_dist = sum(dist)

    seg_tree = SegmentTree(dist)

    ans = 0
    prev_x = events[0].x
    for event in events:
        ans += (sum_dist - seg_tree.query()) * (event.x - prev_x)
        seg_tree.update_range(y_coord_index[event.y1], y_coord_index[event.y2], event.type)
        prev_x = event.x

    print(ans)


if __name__ == "__main__":
    main()
