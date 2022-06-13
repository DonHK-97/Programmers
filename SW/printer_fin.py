def solution(priorities, location):
    answer = 0
    identity = [i for i in range(len(priorities))]
    target = priorities[location]

    while priorities:
        primary = max(priorities)
        temp_pri = priorities.pop(0)
        temp_ident = identity.pop(0)

        if temp_pri < primary:
            priorities.append(temp_pri)
            identity.append(temp_ident)
            continue
        elif temp_pri == primary:
            answer += 1
            if temp_ident == location:
                return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
