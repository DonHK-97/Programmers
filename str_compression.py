def solution(s):

    string_list = s
    final_length = []

    for unit in range(1, len(s)):
        processed_length = []
        processed_string = []

        for index in range(0, len(s), unit):
            last = index + unit

            if last > len(s):
                break

            compare_string = string_list[index: last]

            if compare_string in string_list[index - unit: index]:
                continue

            if compare_string == string_list[last: (last + unit)]:
                result = 1
                for repeat in range(last, len(s) + 1, unit):
                    if compare_string == string_list[repeat: repeat + unit]:
                        result = result + 1
                    else:
                        processed_length.append(result)
                        processed_string.append(compare_string)
                        break
            else:
                continue

        compressed_length = (len(string_list) - sum(processed_length) * unit) + (unit + 1) * len(processed_length) * 2
        final_length.append(compressed_length)
        print(final_length)

    answer = min(final_length)
    return answer

print(solution("aabbaccc"))