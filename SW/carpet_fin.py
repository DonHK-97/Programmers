def solution(brown, yellow):
    answer = []
    sum_pixel = brown + yellow

    for i in range(1, sum_pixel + 1):
        if not sum_pixel % i:
            answer.append(i)

    total = len(answer)
    index = total // 2

    if total % 2:
        return [answer[index]] * 2
    else:
        for i in range(0, index):
            x = answer[index + i]
            y = answer[(index - 1) - i]
            if (x-2)*(y-2) == yellow:
                return [x, y]


print(solution(18, 6))
