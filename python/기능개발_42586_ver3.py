from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1

        if count > 0:
            answer.append(count)

    return answer