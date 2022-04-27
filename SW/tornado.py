def solution(size_n, sand_map):
    tor_loc = [size_n // 2, size_n // 2]
    sand_total = 0
    move = 1

    for row in range(0, size_n):
        sand_total += sum(sand_map[row])

    while sum(tor_loc):
        for turn_iter in range(0, move):
            if move % 2:
                tor_loc[1] -= 1
                sand_map = sand_movement(tor_loc, 'left', sand_map, size_n)
            else:
                tor_loc[1] += 1
                sand_map = sand_movement(tor_loc, 'right', sand_map, size_n)
            if not sum(tor_loc):
                break

        if not sum(tor_loc):
            break

        for turn_iter in range(0, move):
            if move % 2:
                tor_loc[0] += 1
                sand_map = sand_movement(tor_loc, 'down', sand_map, size_n)
            else:
                tor_loc[0] -= 1
                sand_map = sand_movement(tor_loc, 'up', sand_map, size_n)

        move += 1

    for row in range(0, size_n):
        sand_total -= sum(sand_map[row])

    answer = sand_total
    print(answer)
    return answer


def sand_movement(tor_loc, sand_dir, sand_map, size_n):
    tornado_x, tornado_y = tor_loc[0], tor_loc[1]
    sand_stack = sand_map[tornado_x][tornado_y]
    limit = size_n // 2
    move_to, sand_push = sand_direction(sand_dir)

    for row in range(0, size_n):
        for col in range(0, size_n):
            x = tornado_x - limit + row
            y = tornado_y - limit + col

            if not move_to[row][col]:
                continue
            elif x < 0 or y < 0 or x >= size_n or y >= size_n:
                sand_rate = int(sand_map[tornado_x][tornado_y] * move_to[row][col] * 0.01)
                sand_stack -= sand_rate
            else:
                sand_rate = int(sand_map[tornado_x][tornado_y] * move_to[row][col] * 0.01)
                sand_stack -= sand_rate
                sand_map[x][y] += sand_rate

    sand_left_x = tornado_x + sand_push[0]
    sand_left_y = tornado_y + sand_push[1]

    if sand_left_x < 0 or sand_left_y < 0 or sand_left_x >= size_n or sand_left_y >= size_n:
        sand_map[tornado_x][tornado_y] = 0
    else:
        sand_map[sand_left_x][sand_left_y] = sand_stack
        sand_map[tornado_x][tornado_y] = 0
    return sand_map


def sand_direction(direction):
    if direction == 'left':
        move_to = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 0, 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
        sand_push = [0, -1]
    elif direction == 'right':
        move_to = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 0, 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
        sand_push = [0, 1]
    elif direction == 'up':
        move_to = [[0, 0, 5, 0, 0], [0, 10, 0, 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
        sand_push = [-1, 0]
    else:
        move_to = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 0, 10, 0], [0, 0, 5, 0, 0]]
        sand_push = [1, 0]
    return move_to, sand_push


matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 100, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
solution(5, matrix)
