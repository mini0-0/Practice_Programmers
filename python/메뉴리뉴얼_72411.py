from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course:
        all_combs = []
        for order in orders:
            combs = combinations(sorted(order), i)
            all_combs.extend(combs)
        counter = Counter(all_combs)

        if counter:
            max_count = max(counter.values())
            if max_count >= 2:
                for comb, cnt in counter.items():
                    if cnt == max_count:
                        answer.append(''.join(comb))

    return sorted(answer)