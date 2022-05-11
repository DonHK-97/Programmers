def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    if answer == '':
        return participant[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
