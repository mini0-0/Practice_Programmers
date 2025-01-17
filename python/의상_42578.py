def solution(clothes):
    answer = 1
    dic = {}

    for cloth, typ in clothes:
        dic[typ] = dic.get(typ, 0) + 1

    for i in dic:
        answer *= (dic[i] + 1)

    return answer - 1