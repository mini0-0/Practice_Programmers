def solution(participant, completion):
    result = 0
    dic = {}

    for p in participant:
        dic[hash(p)] = p
        result += int(hash(p))

    for c in completion:
        result -= hash(c)
    return dic[result]