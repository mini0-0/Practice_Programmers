import heapq


def get_shortest_dist(graph, start, n):
    dist = [float('inf')] * (n + 1)
    heap = []

    dist[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if dist[current_node] < current_dist:
            continue

        for next_node, time in graph[current_node]:
            new_dist = dist[current_node] + time

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist


def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]

    # 그래프 양방향
    for start, end, time in road:
        graph[start].append((end, time))
        graph[end].append((start, time))

    distance = get_shortest_dist(graph, 1, N)

    for i in range(1, N + 1):
        if distance[i] <= K:
            answer += 1
    return answer
