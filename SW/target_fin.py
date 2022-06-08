def solution(numbers, target):
    no_list = [0]
    answer, index = 0, 0
    count = 2 ** len(numbers) - 1

    while numbers:
        cur_no = numbers.pop()
        cur_len = len(no_list)
        for i in range(index, cur_len):
            temp = no_list[i]
            no_list.append(temp + cur_no)
            no_list.append(temp - cur_no)
        index = cur_len

    no_list = list(no_list[count:])

    for num in no_list:
        if num == target:
            answer += 1

    return answer

print(solution([4, 1, 2, 1], 4))
