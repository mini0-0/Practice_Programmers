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

    visited_r = [[False] * maze_col for _ in range(maze_row)]
    visited_b = [[False] * maze_col for _ in range(maze_row)]
    visited_r[red_start[0]][red_start[1]] = True
    visited_b[blue_start[0]][blue_start[1]] = True

    answer = float('inf')

    def DFS(curr_r, curr_b, turn):
        nonlocal answer

        red_candidates = []
        blue_candidates = []

        if turn >= answer: return

        # red, blue가 target에 위치하면 종료
        if curr_r == red_target and curr_b == blue_target: answer = min(answer, turn)

        # red의 다음으로 이동 가능한 후보 찾기
        if curr_r == red_target:
            red_candidates.append(curr_r)

        else:
            red_x, red_y = curr_r
            for dx, dy in paths:
                nx = red_x + dx
                ny = red_y + dy

                if 0 <= nx < maze_row and 0 <= ny < maze_col and maze[nx][ny] != 5 and not visited_r[nx][ny]:
                    red_candidates.append((nx, ny))

        # blue의 다음으로 이동 가능한 후보 찾기
        if curr_b == blue_target:
            blue_candidates.append(curr_b)

        else:
            blue_x, blue_y = curr_b
            for dx, dy in paths:
                nx = blue_x + dx
                ny = blue_y + dy

                if 0 <= nx < maze_row and 0 <= ny < maze_col and maze[nx][ny] != 5 and not visited_b[nx][ny]:
                    blue_candidates.append((nx, ny))

        # red와 blue 후보들을 통해 이동가능 여부 확인 및 이동 횟수 계산
        for red_nr, red_nc in red_candidates:
            for blue_nr, blue_nc in blue_candidates:
                # 같은 칸 금지
                if (red_nr, red_nc) == (blue_nr, blue_nc):
                    continue

                # red와 blue의 서로 교차 교환 금지
                elif (red_nr, red_nc) == curr_b and (blue_nr, blue_nc) == curr_r:
                    continue

                # 방문 가능한 경우
                red_moved = (red_nr, red_nc) != curr_r
                blue_moved = (blue_nr, blue_nc) != curr_b

                if red_moved: visited_r[red_nr][red_nc] = True
                if blue_moved: visited_b[blue_nr][blue_nc] = True

                DFS((red_nr, red_nc), (blue_nr, blue_nc), turn + 1)

                if red_moved: visited_r[red_nr][red_nc] = False
                if blue_moved: visited_b[blue_nr][blue_nc] = False

    DFS(red_start, blue_start, 0)

    return answer if answer != float('inf') else 0