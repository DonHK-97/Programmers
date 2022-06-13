def solution(operations):
    import heapq as hq

    min_heap = []
    max_heap = []

    for code in operations:
        code, value = code.split(' ')
        value = int(value)

        if code == 'I':
            hq.heappush(min_heap, value)
            hq.heappush(max_heap, (-value, value))
        else:
            if not min_heap:
                continue
            elif value > 0:
                hq.heappop(max_heap)
                min_heap.pop()
            else:
                hq.heappop(min_heap)
                max_heap.pop()

    if min_heap:
        return [max_heap[0][1], min_heap[0]]
    else:
        return [0, 0]


print(solution(["I 7", "I 5", "I -5", "D -1"]))
