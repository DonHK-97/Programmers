def solution(prices):
    answer = []
    num_cost = len(prices)

    for i in range(0, num_cost):
        temp_duration = 0
        for j in range(i + 1, num_cost):
            temp_duration += 1
            if prices[i] > prices[j]:
                break
        answer.append(temp_duration)

    return answer


print(solution([1, 2, 3, 2, 3]))
