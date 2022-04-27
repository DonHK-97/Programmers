def solution(new_id):
    answer = ''
    temp_list = []
    reduction_list = []
    
    new_id = new_id.lower()
    
    for char in new_id:
        if char.isalpha() or char.isdigit() or char in ['-', '_', '.']:
            temp_list.append(char)

    for index, char in enumerate(temp_list):
        if index < (len(temp_list) - 1):
            if char == '.' and temp_list[index + 1] == '.':
                continue
            elif char == '.' and temp_list[index + 1] != '.':
                reduction_list.append(char)
            else:
                reduction_list.append(char)
        else:
            reduction_list.append(char)
    
    answer = ''.join(reduction_list)
    code = 1

    if answer[0] == '.': 
        answer = answer[1:]
        code = code + 1

    if answer == '':
        answer = answer + 'a'
        code = code + 1

    if len(answer) >= 16:
        answer = answer[:15]
        code = code + 1

    if answer[(len(answer)-1)] == '.':
        answer = answer[:-1]
        code = code + 1
            
    while(len(answer) <= 2):
        answer = answer + answer[len(answer)-1]
        
    return answer

str_temp = "hello my name is kdh"
print(len(str_temp))