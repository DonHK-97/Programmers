def solution(s):
    answer = []
    location = -1

    for string in s:
        temp = string.replace("110", '')
        remains = len(temp)
        print(temp)

        if remains:
            for i in reversed(range(remains)):
                if temp[i] == '0':
                    location = i + 1
                    break
        else:
            if temp[0] == '0':
                location = 0

        answer.append(temp[:location] + '110' + temp[location:])

    return answer


print(solution(["1110", "100111100", "0111111010"]))
