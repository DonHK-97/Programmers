def solution(participant, completion):
    # 참가자들의 상태를 기록할 해시
    runner_stats = {}

    # 참여한 상태의 참가자를 1, 동명이인은 추가
    for name in participant:
        if name in runner_stats:
            runner_stats[name] += 1
        else:
            runner_stats[name] = 1

    # 완료해서 경주중이지 않은 참가자를 감산
    for name in completion:
        runner_stats[name] -= 1

    # 아직까지 완료되지 못한 참가자의 이름을 리턴
    for name, stat in runner_stats.items():
        if stat:
            return name


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
