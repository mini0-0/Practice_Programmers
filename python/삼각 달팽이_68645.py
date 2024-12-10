def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    y, x = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            angle = i % 3
            # 반시계 방향 아래 -> 오른쪽 -> 대각선
            if angle == 0:
                y += 1
            elif angle == 1:
                x += 1
            elif angle == 2:
                y -= 1
                x -= 1
            answer[y][x] = num
            num += 1

    return [i for j in answer for i in j]