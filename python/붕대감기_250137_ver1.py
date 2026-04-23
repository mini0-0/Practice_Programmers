from collections import deque


def solution(bandage, health, attacks):
    now_health = health
    attack_succes_cnt = 0

    cast_time, time_heal, bonues_heal = bandage
    attack_q = deque(attacks)
    last_attack_time = attacks[-1][0]

    for time in range(1, last_attack_time + 1):
        # 공격이 있는 경우
        if attack_q and time == attack_q[0][0]:
            attack_time, damage = attack_q.popleft()
            now_health -= damage
            attack_succes_cnt = 0

            if now_health <= 0: return -1
            continue

        # 공격이 없는 경우
        attack_succes_cnt += 1
        now_health += time_heal

        if attack_succes_cnt == cast_time:
            now_health += bonues_heal
            attack_succes_cnt = 0

        now_health = min(now_health, health)

    return now_health