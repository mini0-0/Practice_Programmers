def time_to_seconds(time):
    h, m, s = map(int, time.split(":"))
    time = h * 3600 + m * 60 + s

    return time


def seconds_to_time(time):
    h, rem = divmod(time, 3600)
    m, s = divmod(rem, 60)

    return f"{h:02d}:{m:02d}:{s:02d}"


def solution(play_time, adv_time, logs):
    answer = 0

    # 시분 -> 초로 변경
    play_time_seconds = time_to_seconds(play_time)
    adv_time_seconds = time_to_seconds(adv_time)

    # 누적합 배열 생성
    total_time = [0] * (play_time_seconds + 1)

    for log in logs:
        start_time, end_time = log.split("-")
        start_time_seconds = time_to_seconds(start_time)
        end_time_seconds = time_to_seconds(end_time)
        total_time[start_time_seconds] += 1
        total_time[end_time_seconds] -= 1

    # 각 시점의 동시 시청자 수
    for i in range(1, play_time_seconds + 1):
        total_time[i] += total_time[i - 1]

    # 시청자 수의 누적합
    for i in range(1, play_time_seconds + 1):
        total_time[i] += total_time[i - 1]

    max_value = total_time[adv_time_seconds - 1]

    # 시청자의 누적합에서 최적의 광고 시간 확인
    for start in range(play_time_seconds - adv_time_seconds + 1):
        end = start + adv_time_seconds - 1
        current = total_time[end] - total_time[start - 1]

        if current > max_value:
            max_value = current
            answer = start

    return seconds_to_time(answer)