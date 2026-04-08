import sys

input = sys.stdin.readline

n, k = map(int, input().split())
number_list = list(map(int, input().split()))
pre_sum = [0]
temp = 0
answer = -sys.maxsize

for num in number_list:
    temp = temp + num
    pre_sum.append(temp)

for i in range(n-k+1):
    answer = max(answer, pre_sum[i+k] - pre_sum[i])

print(answer)
