import sys

input = sys.stdin.readline

n, k = map(int, input().split())
number_list = list(map(int, input().split()))

current_sum = sum(number_list[:k])
answer = current_sum

for i in range(k, n):
    current_sum = current_sum + number_list[i] - number_list[i - k]

    if current_sum > answer:
        answer = current_sum

print(answer)