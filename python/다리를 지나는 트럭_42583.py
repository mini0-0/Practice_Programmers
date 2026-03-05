from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    waiting = deque(truck_weights)
    total_weight = 0

    while waiting or total_weight > 0:
        time += 1
        total_weight -= bridge.popleft()

        if waiting:
            if (total_weight + waiting[0]) <= weight:
                bridge.append(waiting[0])
                total_weight += waiting[0]
                waiting.popleft()

            else:
                bridge.append(0)
        else:
            bridge.append(0)

    return time