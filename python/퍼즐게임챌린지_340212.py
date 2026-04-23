def solution(diffs, times, limit):
    low = 1
    high = max(diffs)
    answer = high

    while low <= high:
        mid = (low + high) // 2
        total_time = 0

        for i in range(len(diffs)):
            if total_time > limit: break

            # diff <= level -> time_cur만큼 시간 사용
            if diffs[i] <= mid:
                total_time += times[i]

            # diff > level -> diff-level 틀림, time_cur만큼 시간 이용 추가로 time_prev 만큼 시간을 사용
            elif diffs[i] > mid:
                wrong = diffs[i] - mid
                total_time += (times[i] + times[i - 1]) * wrong + times[i]

        if total_time <= limit:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer