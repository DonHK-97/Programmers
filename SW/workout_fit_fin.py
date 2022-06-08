def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    common = []

    for more in reserve:
        if more in lost:
            common.append(more)

    if common:
        for value in common:
            lost.remove(value)
            reserve.remove(value)

    answer = n - len(lost)

    while reserve:
        temp_index = 0
        remain = reserve.pop(0)

        if remain - 1 in lost:
            lost.remove(remain - 1)
            answer += 1
            continue
        elif remain + 1 in lost:
            lost.remove(remain + 1)
            answer += 1
            continue

        if not reserve:
            return answer

    return answer


print(solution(7, [2, 3, 4], [1, 2, 3, 6]))
