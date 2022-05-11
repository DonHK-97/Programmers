def solution(absolutes, signs):
    answer = 0

    for index, digits in enumerate(absolutes):
        if signs[index]:
            answer += digits
        else:
            answer -= digits

    return answer

print(solution([4,7,12], [True,False,True]))