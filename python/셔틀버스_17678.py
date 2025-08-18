def solution(n, t, m, timetable):
    crew = sorted([int(h) * 60 + int(m) for h, m in (time.split(":") for time in timetable)])
    bus = 9 * 60
    idx = 0

    for i in range(n):
        count = 0

        while idx < len(crew) and crew[idx] <= bus and count < m:
            idx += 1
            count += 1

        if i == n - 1:
            if count < m:
                answer = bus
            else:
                answer = crew[idx - 1] - 1

        bus += t

    return f"{answer // 60:02d}:{answer % 60:02d}"