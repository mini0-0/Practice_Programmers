from itertools import combinations, permutations

def solution(ability):
    answer = 0
    people, sports_size = len(ability), len(ability[0])
    scores = [i for i in range(people)]
    sports = [i for i in range(sports_size)]

    for i in combinations(scores, sports_size):
        for j in permutations(sports, sports_size):
            power = 0
            for k in range(len(j)): power += ability[i[k]][j[k]]
            answer = max(power, answer)

    return answer