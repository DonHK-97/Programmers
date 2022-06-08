def solution(clothes):
    closet = {}
    answer = 1

    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 2

    amount = list(closet.values())
    for value in amount:
        if answer:
            answer *= value

    return answer - 1


print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))
