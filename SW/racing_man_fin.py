def solution(participant, completion):
    runner_stats = {}

    for name in participant:
        if name in runner_stats:
            runner_stats[name] += 1
        else:
            runner_stats[name] = 1

    for name in completion:
        runner_stats[name] -= 1

    for name, stat in runner_stats.items():
        if stat:
            return name


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
