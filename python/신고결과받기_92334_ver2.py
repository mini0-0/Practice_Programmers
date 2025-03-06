def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {uid: [] for uid in id_list}
    stop_count = {uid: 0 for uid in id_list}

    for r in set(report):
        user, target = r.split()
        reports[user].append(target)
        stop_count[target] += 1

    stop_list = {user for user, count in stop_count.items() if count >= k}

    id_map = {uid: idx for idx, uid in enumerate(id_list)}

    for user, targets in reports.items():
        for target in targets:
            if target in stop_list:
                answer[id_map[user]] += 1

    return answer
