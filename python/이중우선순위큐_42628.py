import heapq

def solution(operations):
    q = []  # 양수
    rq = []  # 음수

    for operation in operations:
        alpha, num = operation.split()
        num = int(num)

        if alpha == "I":
            heapq.heappush(q, num)
            heapq.heappush(rq, -num)

        elif alpha == "D":
            if not q:
                continue

            if num == 1:
                max_val = -heapq.heappop(rq)
                q.remove(max_val)

            elif num == -1:
                min_val = heapq.heappop(q)
                rq.remove(-min_val)

    if not q:
        return [0, 0]
    else:
        return [max(q), min(q)]