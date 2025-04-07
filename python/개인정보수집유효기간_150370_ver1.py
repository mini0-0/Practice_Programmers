def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    todays = to_days(today)
    terms_dict = {}

    for t in terms:
        t_type, date = t.split()
        terms_dict[t_type] = int(date)

    for i, p in enumerate(privacies):
        date, t_type = p.split()
        collect_days = to_days(date)
        expire_days = collect_days + terms_dict[t_type] * 28

        if todays >= expire_days:
            answer.append(i + 1)

    return answer