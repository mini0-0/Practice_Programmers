from collections import deque


def bfs(graph, start, visited):
    width, height = len(graph[0]), len(graph)
    paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    size = 0
    cols = set()

    while queue:
        x, y = queue.popleft()

        size += 1
        cols.add(y)

        for dx, dy in paths:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < height) and (0 <= ny < width):
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

    return size, cols


def solution(land):
    width, height = len(land[0]), len(land)
    visited = [[False] * width for _ in range(height)]

    land_cols = [0] * width

    for h in range(height):
        for w in range(width):
            if land[h][w] == 1 and not visited[h][w]:
                size, cols = bfs(land, (h, w), visited)

                for col in cols:
                    land_cols[col] += size

    return max(land_cols)