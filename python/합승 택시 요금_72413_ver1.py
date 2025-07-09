import sys
import heapq


def dijkstra(s, graph, n):
    dist = [sys.maxsize] * (n + 1)
    q = [(0, s)]
    dist[s] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dist[now] < cost:
            continue
        for next_node, next_cost in graph[now]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))

    return dist


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        edge1, edge2, num = fare
        graph[edge1].append((edge2, num))
        graph[edge2].append((edge1, num))

    dist_s = dijkstra(s, graph, n)
    dist_a = dijkstra(a, graph, n)
    dist_b = dijkstra(b, graph, n)

    answer = min(dist_s[i] + dist_a[i] + dist_b[i] for i in range(1, n + 1))
    return answer