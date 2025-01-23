def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack and stack[stack[-1]] > prices[i]:
            past= stack.pop()
            answer[past] = i - past
        stack.append(i)
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer