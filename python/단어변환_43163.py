from collections import deque

def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [0] * len(words)

    while queue:
        word, cnt = queue.popleft()

        if word == target:
            return cnt

        for i in range(len(words)):
            if not visited[i]:
                if sum(x != y for x, y in zip(word, words[i])) == 1:
                    queue.append([words[i], cnt + 1])
                    visited[i] = 1

    return 0