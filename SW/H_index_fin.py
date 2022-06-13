def solution(citations):
    citations.sort(reverse=True)

    for index, cite in enumerate(citations):
        if index >= cite:
            return index
    return len(citations)


print(solution([6, 5, 5, 5, 5, 2, 1, 0]))
