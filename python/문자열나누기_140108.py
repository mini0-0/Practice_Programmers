def solution(s):
    answer = 0
    i = 0
    while i < len(s):
        x = s[i]
        x_count = 1
        other_count = 0
        i += 1
        while i < len(s):
            if s[i] == x:
                x_count += 1
            else:
                other_count += 1
            i += 1
            if x_count == other_count:
                break
        answer += 1

    return answer