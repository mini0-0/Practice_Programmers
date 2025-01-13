def available(n, stones, k):
    skip = 0
    for stone in stones:
        if stone < n:
            skip += 1
            if skip >= k:
                return False
        else:
            skip = 0
    return True


def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)

    while start <= end:
        mid = (start + end) // 2
        if available(mid, stones, k):
            start = mid + 1
            answer = max(answer, mid)
        else:
            end = mid - 1

    return answer


