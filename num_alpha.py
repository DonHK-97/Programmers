def solution(s):
    answer = 0
    num_list = []
    string_to_num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                     'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    index = 0

    while index < len(s):
        letter = s[index]

        if letter.isdigit():
            num_list.append(int(letter))
            index = index + 1
        else:
            for value in range(3, 6):
                temp_string = s[index: index+value]

                if temp_string in string_to_num:
                    num_list.append(string_to_num[temp_string])
                    index = index + value
                    break
                else:
                    continue
    print(num_list)

    for index, number in enumerate(num_list):
        exp = len(num_list) - index -1
        answer = answer + number * (10**exp)

    return answer

print(solution("one4seveneight"))