def solution(n, k, cmd):
    cur = k
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ['O'] * n
    table[0][0] = None
    table[n - 1][1] = None
    stack = []
    for c in cmd:
        if c == 'C':
            # 삭제
            answer[cur] = 'X'
            prev, next_ = table[cur]
            stack.append([prev, cur, next_])

            if prev is not None:
                table[prev][1] = next_
            if next_ is not None:
                table[next_][0] = prev

            del table[cur]
            cur = next_ if next_ is not None else prev

        elif c == 'Z':
            # 복구
            prev, now, next_ = stack.pop()
            answer[now] = 'O'
            table[now] = [prev, next_]
            if prev is not None:
                table[prev][1] = now
            if next_ is not None:
                table[next_][0] = now

        else:
            direct, cnt = c.split()
            cnt = int(cnt)
            if direct == 'U':
                for _ in range(cnt):
                    cur = table[cur][0]

            elif direct == 'D':
                for _ in range(cnt):
                    cur = table[cur][1]

    return ''.join(answer)