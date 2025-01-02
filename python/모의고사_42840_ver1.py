def solution(answers):
    answer = []
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == n1[i % 5]:
            count1 += 1
        if answers[i] == n2[i % 8]:
            count2 += 1
        if answers[i] == n3[i % 10]:
            count3 += 1

    max_n = max(count1, count2, count3)

    if max_n == count1:
        answer.append(1)
    if max_n == count2:
        answer.append(2)
    if max_n == count3:
        answer.append(3)

    return answer