import heapq as hq


def solution(jobs):
    jobs.sort(reverse=True)
    total = len(jobs)

    arrived_list = []
    current_time = 0
    process_time = 0

    while 1:
        while jobs:
            if jobs[-1][0] <= current_time:
                ta, tp = jobs.pop()
                hq.heappush(arrived_list, [tp, ta])
            else:
                break

        if jobs and not arrived_list:
            current_time += 1
            continue

        current_task = hq.heappop(arrived_list)
        current_time += current_task[0]
        process_time += current_time - current_task[1]

        #print(current_task, current_time, process_time, arrived_list)

        if not jobs and not arrived_list:
            return process_time // total



print(solution([[0, 3], [1, 3], [7, 6]]))
