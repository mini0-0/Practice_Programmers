from collections import deque, defaultdict
from itertools import permutations
import copy

path = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(board, start, target):
    visited = [[False] * 4 for _ in range(4)]
    queue = deque()
    queue.append((*start, 0))
    visited[start[0]][start[1]] = True

    while queue:
        x, y, move = queue.popleft()
        if (x, y) == target:
            return move

        for dx, dy in path:
            # 일반 이동
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, move + 1))

            # Ctrl 이동
            cx, cy = x, y
            while True:
                nx, ny = cx + dx, cy + dy
                if not (0 <= nx < 4 and 0 <= ny < 4):
                    break
                cx, cy = nx, ny
                if board[cx][cy] != 0:
                    break
            if not visited[cx][cy]:
                visited[cx][cy] = True
                queue.append((cx, cy, move + 1))

    return float('inf')


def dfs(board, cur, orders, graph, depth, move_sum, min_move):
    if depth == len(orders):
        min_move[0] = min(min_move[0], move_sum)
        return

    num = orders[depth]
    first, second = graph[num]

    # first -> second
    dist1 = bfs(board, cur, first)
    dist2 = bfs(board, first, second)

    board[first[0]][first[1]] = 0
    board[second[0]][second[1]] = 0

    dfs(board, second, orders, graph, depth + 1, move_sum + dist1 + dist2 + 2, min_move)

    board[first[0]][first[1]] = num
    board[second[0]][second[1]] = num

    # second -> first
    dist1 = bfs(board, cur, second)
    dist2 = bfs(board, second, first)

    board[first[0]][first[1]] = 0
    board[second[0]][second[1]] = 0

    dfs(board, first, orders, graph, depth + 1, move_sum + dist1 + dist2 + 2, min_move)

    board[first[0]][first[1]] = num
    board[second[0]][second[1]] = num


def solution(board, r, c):
    graph = defaultdict(list)

    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                graph[board[i][j]].append((i, j))

    min_move = [float('inf')]

    for orders in permutations(graph.keys()):
        temp_board = copy.deepcopy(board)
        dfs(temp_board, (r, c), orders, graph, 0, 0, min_move)

    return min_move[0]