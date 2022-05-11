def solution(progresses, speeds):
    answer = []
    while progresses:
        count = 0

        for index in range(len(progresses)):
            progresses[index] += speeds[index]

        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                count += 1
            else:
                break

        if count:
            answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
