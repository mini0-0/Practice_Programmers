from collections import deque

def solution(maze):
    maze_row, maze_col = len(maze), len(maze[0])
    paths = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(maze_row):
        for j in range(maze_col):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_target = (i, j)
            elif maze[i][j] == 4:
                blue_target = (i, j)

    def get_candidates(curr, target, visited):
        # red, blue가 target에 위치하면 종료
        if curr == target:
            return [curr]

        candidates = []
        x, y = curr
        for dx, dy in paths:
            nx, ny = x + dx, y + dy
            if 0 <= nx < maze_row and 0 <= ny < maze_col:
                if maze[nx][ny] != 5 and (nx, ny) not in visited:
                    candidates.append((nx, ny))
        return candidates

    q = deque()
    q.append((red_start, blue_start, frozenset([red_start]), frozenset([blue_start]), 0))

    while q:
        curr_r, curr_b, visited_r, visited_b, turn = q.popleft()

        if curr_r == red_target and curr_b == blue_target:
            return turn

        red_candidates = get_candidates(curr_r, red_target, visited_r)
        blue_candidates = get_candidates(curr_b, blue_target, visited_b)

        # red와 blue 후보들을 통해 이동가능 여부 확인 및 이동 횟수 계산
        for red_next in red_candidates:
            for blue_next in blue_candidates:
                # 같은 칸 금지
                if red_next == blue_next:
                    continue

                # red와 blue의 서로 교차 교환 금지
                if red_next == curr_b and blue_next == curr_r:
                    continue

                new_visited_r = visited_r
                new_visited_b = visited_b

                if red_next != curr_r:
                    new_visited_r = visited_r | {red_next}
                if blue_next != curr_b:
                    new_visited_b = visited_b | {blue_next}

                q.append((red_next, blue_next, new_visited_r, new_visited_b,turn + 1))

    return 0