def solution(array, commands):
    answer = []
    for lane in commands:
        start, end, th = lane
        temp_arr = list(array[start-1: end])
        temp_arr.sort()
        answer.append(temp_arr[th-1])

    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

