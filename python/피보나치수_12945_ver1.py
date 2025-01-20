def solution(n):
    answer=[0,1]
    for i in range(2,n+1):
        f=answer[i-1] + answer[i-2]
        answer.append(f % 1234567)
    return answer[n]