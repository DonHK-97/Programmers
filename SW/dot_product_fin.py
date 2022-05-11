def solution(a, b):
    answer = 0

    for index, digit in enumerate(a):
        answer += digit * b[index]

    return answer
