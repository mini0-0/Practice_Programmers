from collections import Counter


def solution(points, routes):
    rob_paths = []

    for route in routes:
        time = 0

        curr_r, curr_c = points[route[0] - 1]
        rob_paths.append((time, curr_r, curr_c))

        for i in range(1, len(route)):
            target_r, target_c = points[route[i] - 1]

            while curr_r != target_r or curr_c != target_c:
                if curr_r != target_r:
                    curr_r += 1 if curr_r < target_r else -1
                elif curr_c != target_c:
                    curr_c += 1 if curr_c < target_c else -1

                time += 1
                rob_paths.append((time, curr_r, curr_c))

    counts = Counter(rob_paths)
    return sum(1 for v in counts.values() if v >= 2)
