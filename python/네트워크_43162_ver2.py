def dfs(computers, visited, start):
    stack = [start]
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            visited[cur] = 1
        for i in range(len(computers)):
            if computers[cur][i] == 1 and not visited[i]:
                stack.append(i)

def solution(n, computers):
    visited = [0] * n
    answer = 0
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    return answer
