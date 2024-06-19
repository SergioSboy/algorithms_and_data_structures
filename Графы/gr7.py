INF = 10 ** 9


def floyd_warshall(graph, N):
    dist = [[INF] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                dist[i][j] = 0
            elif (i, j) in graph:
                dist[i][j] = graph[(i, j)]


    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


    return dist


def main():
    N, M = map(int, input().split())
    graph = {}

    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[(u - 1, v - 1)] = w
        graph[(v - 1, u - 1)] = w


    dist = floyd_warshall(graph, N)

    min_sum = INF
    min_city = -1

    for i in range(N):
        max_dis = max(dist[i])

        if max_dis < min_sum:
            min_sum = max_dis
            min_city = i + 1

    print(min_city)


if __name__ == "__main__":
    main()
