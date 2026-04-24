def solution(mats, park):
    row, col = len(park), len(park[0])
    dp = [[0] * col for _ in range(row)]
    mats = sorted(mats, reverse=True)
    max_size = 0
    for y in range(len(park)):
        for x in range(len(park[0])):
            if park[y][x] != "-1":
                continue

            elif y == 0 or x == 0:
                dp[y][x] = 1

            else:
                dp[y][x] = min(dp[y - 1][x - 1], dp[y - 1][x], dp[y][x - 1]) + 1

            max_size = max(max_size, dp[y][x])

    for m in mats:
        if m <= max_size:
            return m

    return -1
