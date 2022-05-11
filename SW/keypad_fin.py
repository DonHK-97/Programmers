def solution(numbers, hand):
    answer = ''

    num_pad = {1: [0, 0], 2: [0, 1], 3: [0, 2],
               4: [1, 0], 5: [1, 1], 6: [1, 2],
               7: [2, 0], 8: [2, 1], 9: [2, 2],
               0: [3, 1]}
    l_finger = [3, 0]
    r_finger = [3, 2]

    while numbers:
        cur_loc = num_pad[numbers.pop(0)]
        l_dis = distance(cur_loc, l_finger)
        r_dis = distance(cur_loc, r_finger)

        if not cur_loc[1]:
            answer += 'L'
            l_finger = cur_loc
            continue
        elif cur_loc[1] == 2:
            answer += 'R'
            r_finger = cur_loc
            continue

        if l_dis < r_dis:
            answer += 'L'
            l_finger = cur_loc
        elif l_dis > r_dis:
            answer += 'R'
            r_finger = cur_loc
        else:
            if hand == 'left':
                answer += 'L'
                l_finger = cur_loc
            else:
                answer += 'R'
                r_finger = cur_loc

    return answer


def distance(loc1, loc2):
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
