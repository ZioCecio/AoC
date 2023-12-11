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

    
curr_pos = adiacent_start[0]
prev_pos = start_pos

cont = 1
while curr_pos != start_pos:
    matrix[curr_pos[0]][curr_pos[1]][1] = min(matrix[curr_pos[0]][curr_pos[1]][1], cont)
    cont += 1

    temp = curr_pos
    curr_pos = get_next(curr_pos, prev_pos)
    prev_pos = temp
matrix[start_pos[0]][start_pos[1]][1] = 0

double_matrix = []
for i in range(len(matrix) * 2):
    double_matrix.append([])
    for j in range(len(matrix[0]) * 2):
        double_matrix[i].append(' ')

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        cell = matrix[i][j]

        if cell[1] == float('inf'):
            double_matrix[i * 2][j * 2] = '.'
            continue

        if cell[0] == '|':
            double_matrix[i * 2][j * 2] = '|'
            double_matrix[(i * 2) + 1][j * 2] = '|'
        elif cell[0] == '-':
            double_matrix[i * 2][j * 2] = '-'
            double_matrix[i * 2][(j * 2) + 1] = '-'
        elif cell[0] == 'L':
            double_matrix[i * 2][j * 2] = '|'
            double_matrix[(i * 2) + 1][j * 2] = 'L'
            double_matrix[i * 2][(j * 2) + 1] = '-'
        elif cell[0] == 'F':
            double_matrix[i * 2][j * 2] = 'F'
            double_matrix[(i * 2) + 1][j * 2] = '|'
            double_matrix[i * 2][(j * 2) + 1] = '-'
        elif cell[0] == 'J':
            double_matrix[(i * 2) + 1][j * 2] = '-'
            double_matrix[i * 2][(j * 2) + 1] = '|'
            double_matrix[(i * 2) + 1][(j * 2) + 1] = 'J'
        elif cell[0] == '7':
            double_matrix[i * 2][j * 2] = '-'
            double_matrix[i * 2][(j * 2) + 1] = '7'
            double_matrix[(i * 2) + 1][(j * 2) + 1] = '|'

ans = 0
for i in range(len(double_matrix)):
    is_inside = False
    for j in range(len(double_matrix[0])):
        c = double_matrix[i][j]

        if c == '|':
            is_inside = not is_inside
        elif c == '.' and is_inside:
            ans += 1

print(ans)