from collections import deque

def bfs(x, y, visited, board, target):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    shape = [(x, y)]

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<len(board) and 0<=ny<len(board) and not visited[nx][ny] and board[nx][ny] == target:
                visited[nx][ny] = True
                queue.append((nx, ny))
                shape.append((nx, ny))
    return shape

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    normalized = sorted((x - min_x, y - min_y) for x, y in shape)
    return normalized

def rotate(shape):
    return [ (y, -x) for x, y in shape ]

def extract_shapes(board, target):
    visited = [[False]*len(board) for _ in range(len(board))]
    shapes = []
    for i in range(len(board)):
        for j in range(len(board)):
            if not visited[i][j] and board[i][j] == target:
                shape = bfs(i, j, visited, board, target)
                shapes.append(normalize(shape))
    return shapes

def match_puzzle(empty, puzzle_shapes, used):
    for i, puzzle in enumerate(puzzle_shapes):
        if used[i]:
            continue
        rotated = puzzle
        for _ in range(4):
            rotated = rotate(rotated)
            if normalize(rotated) == empty:
                used[i] = True
                return len(empty)
    return 0

def solution(game_board, table):
    empty_spaces = extract_shapes(game_board, 0)
    puzzle_shapes = extract_shapes(table, 1)
    used = [False] * len(puzzle_shapes)
    answer = 0

    for empty in empty_spaces:
        answer += match_puzzle(empty, puzzle_shapes, used)

    return answer