def solution(bridge_length, weight, truck_weights):
    answer = 1
    bridge_status = [0] * bridge_length
    truck_weights.reverse()
    bridge_status[0] = truck_weights.pop()
    bridge_total = bridge_status[0]

    while 1:
        answer += 1
        temp = bridge_status.pop()
        if temp:
            bridge_total -= temp

        if not bridge_total and not truck_weights:
            return answer

        if truck_weights:
            if bridge_total + truck_weights[-1] <= weight:
                temp = truck_weights.pop()
                bridge_status.insert(0, temp)
                bridge_total += temp
            else:
                bridge_status.insert(0, 0)
        else:
            bridge_status.insert(0, 0)

print(solution(2, 10, [7, 4, 5, 6]))
