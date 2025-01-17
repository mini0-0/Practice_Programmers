def solution(record):
    answer = []
    actions = []
    user = {}

    for r in record:
        info = r.split()
        cmd, uid = info[0], info[1]

        if cmd in ("Enter", "Change"):
            user[uid] = info[2]
        actions.append((cmd, uid))

    for a in actions:
        cmd, uid = a
        if cmd == "Enter":
            answer.append(f'{user[uid]}님이 들어왔습니다.')
        elif cmd == "Leave":
            answer.append(f'{user[uid]}님이 나갔습니다.')

    return answer