def dfs(numbers, step, total, target):
    if step == len(numbers):
        if total == target:
            return 1
        else:
            return 0

    answer = 0
    answer += dfs(numbers, step + 1, total + numbers[step], target)
    answer += dfs(numbers, step + 1, total - numbers[step], target)

    return answer


def solution(numbers, target):
    return dfs(numbers, 0, 0, target)

