def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance

    rocks.append(distance)  # 최종 거리 추가
    rocks.sort()  # 징검다리 정렬

    while start <= end:
        mid = (start + end) // 2
        del_rock = 0  # 지워야할 바위
        pre_rock = 0  # 이전 바위

        for rock in rocks:
            if rock - pre_rock < mid:
                del_rock += 1
            else:
                pre_rock = rock

            if del_rock > n:
                break

        if del_rock > n:  # 제거한 바위 > 목표로 지워야할 바위
            end = mid - 1

        else:
            answer = mid
            start = mid + 1

    return answer


