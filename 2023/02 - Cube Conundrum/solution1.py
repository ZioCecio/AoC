file = open('input.txt')

color_limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

ans = 0
for line in file.readlines():
    [game, moves] = line.split(':')
    game_id = int(game.split(' ')[1])

    is_valid = True
    for move in moves.split(';'):
        cubes_info = move.split(',')

        for cube_info in cubes_info:
            [number, color] = cube_info.strip().split(' ')

            if color_limits[color] < int(number):
                is_valid = False
                break

        if not is_valid:
            break

    if is_valid:
        ans += game_id

print(ans)