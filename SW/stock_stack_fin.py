def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for index, cost in enumerate(prices):
        while stack:
            if cost >= prices[stack[-1]]:
                break
            identity = stack.pop()
            answer[identity] = index - identity
        stack.append(index)

    while stack:
        identity = stack.pop()
        answer[identity] = len(prices) - 1 - identity

    return answer

print(solution([1,2,3,2,3]))
