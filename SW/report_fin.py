def solution(id_list, report, k):
    answer = []
    user_no = len(id_list)
    user_dict = {name : index for index, name in enumerate(id_list)}
    data_record = [[0 for col in range(0, user_no)] for row in range(0, user_no)]
    answer = [0 for user in range(0, user_no)]
    
    for log in report:
        id_target = log.find(' ')
        user = log[:id_target]
        target = log[id_target+1:]
        
        user = user_dict[user]
        target = user_dict[target]
        
        if data_record[target][user]:
            continue
        else:
            data_record[target][user] = 1
            
    for user in range(0, user_no):
        temp = sum(data_record[user])
        if temp >= k:
            for index, code in enumerate(data_record[user]):
                if code: answer[index] = answer[index] + 1
            
    return answer