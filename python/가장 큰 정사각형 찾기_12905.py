def solution(board):
    answer = max(max(row) for row in board)

    for row in range(1, len(board)):
        for col in range(1, len(board[0])):
                     if board[row][col] == 1 :
                        board[row][col] = min(board[row-1][col], board[row][col-1], board[row-1][col-1]) + 1
                        answer = max(answer, board[row][col])

    return answer ** 2