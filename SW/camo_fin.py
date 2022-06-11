def solution(clothes):
    # 해시인 딕셔너리를 생성
    closet = {}
    answer = 1

    # 옷이 하나 존재하는 것으로 옷이 없다는 경우의 수를 포함하여 생성되기 때문에 2로 초기화
    for cloth in clothes:
        if cloth[1] in closet:
            closet[cloth[1]] += 1
        else:
            closet[cloth[1]] = 2

    # 카테고리 별, 옷의 가짓수를 모두 곱해 총 경우의 수를 계산한다.
    for value in closet.values():
        answer *= value

    # 옷이 아예 존재하지 않는다는 경우의 수를 제외
    return answer - 1


print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
