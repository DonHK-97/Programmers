import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if scoville:
        smallest = heapq.heappop(scoville)
        if not scoville:
            return -1
    else:
        return -1

    while smallest < K:
        smaller = heapq.heappop(scoville)
        heapq.heappush(scoville, meta_score(smallest, smaller))
        answer += 1

        smallest = heapq.heappop(scoville)

        if smallest >= K:
            return answer
        elif not scoville:
            return -1

    return answer


def meta_score(x, y):
    return x + y * 2


print(solution([1, 2, 3], 11))
