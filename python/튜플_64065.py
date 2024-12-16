def solution(s):
    answer = {}
    s = sorted(s[2:-2].split("},{"), key=len)
    for i in s:
        li = i.split(",")
        for l in li:
            num = int(l)
            if num not in answer:
                answer[num] = 1

    return list(answer)