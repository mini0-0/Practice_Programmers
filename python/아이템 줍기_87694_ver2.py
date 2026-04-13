from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    xs, ys = set(), set()
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2, x2 * 2 + 1): xs.add(x)
        for y in range(y1 * 2, y2 * 2 + 1): ys.add(y)

    xs.update([characterX * 2, itemX * 2])
    ys.update([characterY * 2, itemY * 2])

    sorted_x = sorted(list(xs))
    sorted_y = sorted(list(ys))

    dict_x = {x: i for i, x in enumerate(sorted_x)}
    dict_y = {y: i for i, y in enumerate(sorted_y)}

    X_LEN, Y_LEN = len(sorted_x), len(sorted_y)
    graph = [[0] * Y_LEN for _ in range(X_LEN)]

    for x1, y1, x2, y2 in rectangle:
        ix1, ix2 = dict_x[x1 * 2], dict_x[x2 * 2]
        iy1, iy2 = dict_y[y1 * 2], dict_y[y2 * 2]

        for i in range(ix1, ix2 + 1):
            for j in range(iy1, iy2 + 1):
                if ix1 < i < ix2 and iy1 < j < iy2:
                    graph[i][j] = 2
                elif graph[i][j] != 2:
                    graph[i][j] = 1

    queue = deque([(dict_x[characterX * 2], dict_y[characterY * 2], 0)])
    graph[dict_x[characterX * 2]][dict_y[characterY * 2]] = 0

    target_x, target_y = dict_x[itemX * 2], dict_y[itemY * 2]

    while queue:
        cx, cy, dist = queue.popleft()

        if cx == target_x and cy == target_y:
            return dist // 2

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < X_LEN and 0 <= ny < Y_LEN and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny, dist + 1))

    return 0