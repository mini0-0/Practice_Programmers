def from_base(num, base):  # n진수 -> 10진수
    value = 0

    for n in num:
        digit = int(n)
        value = value * base + digit

    return value


def to_base(num, base):  # 10진수 -> n진수
    if num == 0: return "0"

    result = ""

    while num > 0:
        remain = num % base
        result = str(remain) + result
        num //= base

    return result


def solution(expressions):
    answer = []
    base_list = {2, 3, 4, 5, 6, 7, 8, 9}

    result_num = []
    result_x = []

    max_digit = 0

    for express in expressions:
        x1, op, x2, eq, r = express.split()

        if r == 'X':
            result_x.append((x1, op, x2, r))
        else:
            result_num.append((x1, op, x2, r))

        # 가장 큰 자리수의 길이
        for char in x1 + x2 + (r if r != 'X' else ''):
            max_digit = max(max_digit, int(char))

    # max_digit 이하의 값은 삭제
    base_list = {b for b in base_list if b > max_digit}

    valid_bases = set()
    # num을 통해서 진법 찾음
    for base in base_list:
        is_possible = True

        for x1, op, x2, r in result_num:
            n_x1 = from_base(x1, base)
            n_x2 = from_base(x2, base)
            n_r = from_base(r, base)

            if op == '+' and n_x1 + n_x2 != n_r:
                is_possible = False
                break

            elif op == '-' and n_x1 - n_x2 != n_r:
                is_possible = False
                break

        if is_possible:
            valid_bases.add(base)

    # valid_base를 돌면서 최종 X값 저장
    for x1, op, x2, r in result_x:
        results = set()

        for base in valid_bases:
            v1 = from_base(x1, base)
            v2 = from_base(x2, base)

            if op == '+':
                res_digit = v1 + v2
            else:
                res_digit = v1 - v2

            results.add(to_base(res_digit, base))

        if len(results) == 1:
            final_r = list(results)[0]

        else:
            final_r = "?"

        answer.append(f"{x1} {op} {x2} = {final_r}")

    return answer