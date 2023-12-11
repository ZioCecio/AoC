file = open('input.txt')

matrix = []
lines = file.readlines()

start_pos = None
for i in range(len(lines)):
    line = lines[i].strip()

    matrix.append([])
    for j in range(len(line)):
        c = line[j]
        if c == 'S':
            start_pos = [i, j]

        matrix[i].append([c, float('inf')])

def get_next(curr, prev):
    curr_symbol = matrix[curr[0]][curr[1]][0]
    if curr_symbol == '-':
        if prev[1] == curr[1] - 1:
            return [curr[0], curr[1] + 1]
        return [curr[0], curr[1] - 1]

    if curr_symbol == '|':
        if prev[0] == curr[0] - 1:
            return [curr[0] + 1, curr[1]]
        return [curr[0] - 1, curr[1]]

    if curr_symbol == 'F':
        if prev[0] == curr[0] + 1:
            return [curr[0], curr[1] + 1]
        return [curr[0] + 1, curr[1]]

    if curr_symbol == 'J':
        if prev[0] == curr[0] - 1:
            return [curr[0], curr[1] - 1]
        return [curr[0] - 1, curr[1]]
    
    if curr_symbol == '7':
        if prev[0] == curr[0] + 1:
            return [curr[0], curr[1] - 1]
        return [curr[0] + 1, curr[1]]
    
    if curr_symbol == 'L':
        if prev[0] == curr[0] - 1:
            return [curr[0], curr[1] + 1]
        return [curr[0] - 1, curr[1]]


north = matrix[start_pos[0] - 1][start_pos[1]][0]
south = matrix[start_pos[0] + 1][start_pos[1]][0]
east = matrix[start_pos[0]][start_pos[1] - 1][0]
west = matrix[start_pos[0]][start_pos[1] + 1][0]

adiacent_start = []
if start_pos[0] > 0 and north != '.' and north in ['|', 'F', '7']:
    adiacent_start.append([start_pos[0] - 1, start_pos[1]])
if start_pos[0] < len(matrix) and south != '.' and south in ['|', 'L', 'J']:
    adiacent_start.append([start_pos[0] + 1, start_pos[1]])
if start_pos[1] > 0 and east != '.' and east in ['-', 'F', 'L']:
    adiacent_start.append([start_pos[0], start_pos[1] - 1])
if start_pos[1] < len(matrix[0]) and west != '.' and west in ['-', '7', 'J']:
    adiacent_start.append([start_pos[0], start_pos[1] + 1])

ans = 0
for adj in adiacent_start:
    curr_pos = adj
    prev_pos = start_pos

    cont = 1
    while curr_pos != start_pos:
        matrix[curr_pos[0]][curr_pos[1]][1] = min(matrix[curr_pos[0]][curr_pos[1]][1], cont)
        cont += 1

        temp = curr_pos
        curr_pos = get_next(curr_pos, prev_pos)
        prev_pos = temp

ans = 0
for line in matrix:
    for cell in line:
        if cell[1] == float('inf'):
            continue
        ans = max(ans, cell[1])

print(ans)