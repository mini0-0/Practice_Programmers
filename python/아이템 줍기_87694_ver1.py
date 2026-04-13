from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * 102 for _ in range(102)]
    paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 2배의 그래프 생성
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2

        # 0: 방문X, 1: 테두리, 2: 내부 값
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    graph[x][y] = 2
                elif graph[x][y] != 2:
                    graph[x][y] = 1

    # BFS로 최소 경로 찾기
    start_x, start_y = characterX * 2, characterY * 2
    target_x, target_y = itemX * 2, itemY * 2

    queue = deque()
    queue.append((start_x, start_y, 0))
    graph[start_x][start_y] = 0

    while queue:
        x, y, dist = queue.popleft()

        if x == target_x and y == target_y:
            return dist // 2

        for dx, dy in paths:
            nx, ny = x + dx, y + dy

            if (0 <= nx < 102) and (0 <= ny < 102) and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny, dist + 1))

    return 0