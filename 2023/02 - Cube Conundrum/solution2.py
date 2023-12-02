file = open('input.txt')

ans = 0
for line in file.readlines():
    [game, moves] = line.split(':')
    game_id = int(game.split(' ')[1])

    color_mins = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }

    for move in moves.split(';'):
        cubes_info = move.split(',')

        for cube_info in cubes_info:
            [number, color] = cube_info.strip().split(' ')
            color_mins[color] = max(color_mins[color], int(number))

    ans += (color_mins['red'] * color_mins['green'] * color_mins['blue'])

print(ans)