def solution(board, moves):
    row = len(board)
    col = len(board[0])
    basket = []
    prev = 0
    answer = 0

    trans_board = [[0 for i in range(row)] for j in range(col)]

    for i in range(row):
        for j in range(col):
            trans_board[j][i] = board[i][j]

    while moves:
        lane = moves.pop(0)

        for index, item in enumerate(trans_board[lane - 1]):
            if item:
                if basket:
                    prev = basket[-1]
                    if prev == item:
                        answer += 1
                        basket.pop(-1)
                        trans_board[lane - 1][index] = 0
                        break
                    else:
                        basket.append(item)
                        trans_board[lane - 1][index] = 0
                        break
                else:
                    basket.append(item)
                    trans_board[lane - 1][index] = 0
                    break

    return answer * 2


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
