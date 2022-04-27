def solution(record):
    status_log = []
    uid_log = []
    uid_name = {}

    answer = []

    for log_string in record:
        log = log_string.split(' ')
        temp_state = log[0]
        temp_uid = log[1]

        if len(log) > 2:
            uid_name[temp_uid] = log[2]

        status_log.append(temp_state)
        uid_log.append(temp_uid)

    for index, status in enumerate(status_log):
        uid = uid_log[index]

        if status == 'Enter':
            answer_status = '들어왔습니다.'
        elif status == 'Leave':
            answer_status = '나갔습니다.'
        else:
            continue

        answer_string = uid_name[uid] + '님이 ' + answer_status
        answer.append(answer_string)

    return answer

string_1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(string_1))