def solution(genres, plays):
    answer = []
    music = {}
    rank = {}
    index = 0

    for genre, play in zip(genres, plays):
        if genre in music:
            music[genre].append((index, play))
            rank[genre] += play
        else:
            music[genre] = [(index, play)]
            rank[genre] = play
        index += 1

    for genre in list(music.keys()):
        music[genre].sort(key=lambda x: (-x[1], x[0]))

    rank = sorted(rank, key=lambda x: rank[x], reverse=True)

    for genre in rank:
        if len(music[genre]) >= 2:
            for i in range(2):
                answer.append(music[genre][i][0])
        else:
            answer.append(music[genre][0][0])

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
