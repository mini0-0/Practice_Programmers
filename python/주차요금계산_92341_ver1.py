from math import ceil

def to_min(first, second):
    fh, fm = map(int, first.split(':'))
    sh, sm = map(int, second.split(':'))

    return (sh * 60 + sm) - (fh * 60 + fm)


def solution(fees, records):
    answer = []
    dt, df, ut, uf = fees
    check, check_time = dict(), dict()

    for record in records:
        time, car, status = record.split()
        if status == "IN":
            check[car] = time
        else:
            check_time[car] = check_time.get(car, 0) + to_min(check[car], time)
            check[car] = status

    for key, value in check.items():
        if value != 'OUT':
            check_time[key] = check_time.get(key, 0) + to_min(value, "23:59")

    check_time = sorted(check_time.items())

    for car, time in check_time:
        if time <= dt:
            answer.append(df)
        else:
            answer.append(df + ceil((time - dt) / ut) * uf)

    return answer