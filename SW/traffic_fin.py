def solution(lines):
    time_cost = []
    answer = []

    for string in lines:
        hour = int(string[11:13]) * 3600000
        minute = int(string[14:16]) * 60000
        second = float(string[17:23]) * 1000

        time_line = hour + minute + int(second)

        init_t = time_line - int(float(string[24:-1]) * 1000) + 1
        temp_list = [init_t, time_line]
        time_cost.append(temp_list)

    session = len(time_cost)

    for index, state in enumerate(time_cost):
        from_init, from_term = state[0], state[1]
        to_init, to_term = from_init + 999, from_term + 999
        count_init, count_to = 0, 0

        for i in range(index, session):
            time_line = time_cost[i]

            if from_init - time_line[1] <= 0 and to_init - time_line[0] >= 0:
                count_init += 1
            if from_term - time_line[1] <= 0 and to_term - time_line[0] >= 0:
                count_to += 1

        answer.append(max(count_init, count_to))

    return max(answer)


print(solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]))
