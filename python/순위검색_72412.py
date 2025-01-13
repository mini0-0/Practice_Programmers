from itertools import combinations
from collections import defaultdict
from bisect import bisect_left as left_bound


def solution(info, query):
    # 1. 미리 덱셔너리 데이터를 만들어 놓을 변수를 선언
    answer = []
    people = defaultdict(list)

    # 2. 주어진 모든 지원자의 데이터를 for문으로 순회하면서 가능한 경우의 수를 딕셔너리에 기록
    for i in info:
        data = i.split()  # info 분리
        score = int(data.pop())  # info 에서 점수제거
        people[''.join(data)].append(score)

        # 4가지 조건에 따른 조합
        # ex) java backend junior pizza 150인 지원자가
        #      -   backend junior pizza 150도 가능함
        # 즉 16가지의 경우에 수가 있음
        for j in range(4):
            candi = list(combinations(data, j))
            for c in candi:
                people[''.join(c)].append(score)

    # 3. 기록한 딕셔너리의 성적 데이터를 모두 정렬
    for i in people:
        people[i].sort()

        # 4. 문의 조건에 따라 검색, 나온 결과의 성적 배열을 이진 탐색하여 몇명인지 확인
    for q in query:
        key = q.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')
        answer.append(len(people[key]) - left_bound(people[key], score))

    return answer


