def solution(answers):
    answer = []
    player = [0, 0, 0]

    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for index, ans in enumerate(answers):
        if p1[index % 5] == ans:
            player[0] += 1
        if p2[index % 8] == ans:
            player[1] += 1
        if p3[index % 10] == ans:
            player[2] += 1

    best = max(player)
    for index, score in enumerate(player):
        if score == best:
            answer.append(index + 1)

    return answer


print(solution([1, 3, 2, 4, 2]))
