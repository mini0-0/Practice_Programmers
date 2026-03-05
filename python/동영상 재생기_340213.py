def solution(video_len, pos, op_start, op_end, commands):
    def to_seconds(time):
        m, s = map(int, time.split(":"))
        return m * 60 + s

    v_len = to_seconds(video_len)
    p = to_seconds(pos)
    o_start = to_seconds(op_start)
    o_end = to_seconds(op_end)

    def skip_opening(current_pos):
        if o_start <= p <= o_end: return o_end
        return current_pos

    for command in commands:
        p = skip_opening(p)

        if command == "prev":
            p = max(0, p - 10)

        elif command == "next":
            p = min(v_len, p + 10)

        p = skip_opening(p)

    m, s = divmod(p, 60)
    return f"{m:02d}:{s:02d}"