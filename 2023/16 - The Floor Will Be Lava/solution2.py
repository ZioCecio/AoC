file = open('input.txt')

matrix = []
for line in file.readlines():
    line = line.strip()
    matrix.append(list(line))

def move(i, j, direction):
    if i < 0 or i >= len(matrix):
        return
    
    if j < 0 or j >= len(matrix[0]):
        return

    if state[i][j][1] == None:
        state[i][j] = ['#', [direction]]
    elif state[i][j][0] == '#' and direction not in state[i][j][1]:
        state[i][j][1].append(direction)
    else:
        return

    new_i = i
    new_j = j
    if direction == 'u':
        new_i -= 1
    if direction == 'd':
        new_i += 1
    if direction == 'l':
        new_j -= 1
    if direction == 'r':
        new_j += 1

    if matrix[i][j] == '.':
        move(new_i, new_j, direction)
    elif matrix[i][j] == '-' and direction in ['u', 'd']:
        move(i, j + 1, 'r')
        move(i, j - 1, 'l')
    elif matrix[i][j] == '-' and direction in ['r', 'l']:
        move(new_i, new_j, direction)
    elif matrix[i][j] == '|' and direction in ['r', 'l']:
        move(i - 1, j, 'u')
        move(i + 1, j, 'd')
    elif matrix[i][j] == '|' and direction in ['u', 'd']:
        move(new_i, new_j, direction)
    elif matrix[i][j] == '/':
        if direction == 'u':
            move(i, j + 1, 'r')
        elif direction == 'd':
            move(i, j - 1, 'l')
        elif direction == 'l':
            move(i + 1, j, 'd')
        elif direction == 'r':
            move(i - 1, j, 'u')
    elif matrix[i][j] == '\\':
        if direction == 'u':
            move(i, j - 1, 'l')
        elif direction == 'd':
            move(i, j + 1, 'r')
        elif direction == 'l':
            move(i - 1, j, 'u')
        elif direction == 'r':
            move(i + 1, j, 'd')

def get_count():
    cont = 0
    for x in state:
        for y in x:
            cont += 1 if y[0] == '#' else 0
    
    return cont

state = []
def reset_state():
    s = []
    for _ in range(len(matrix)):
        s.append([['.', None]] * len(matrix))

    return s

import sys
sys.setrecursionlimit(4000)

ans = 0
for x in range(len(matrix)):
    state = reset_state()
    move(0, x, 'd')
    ans = max(ans, get_count())

    state = reset_state()
    move(len(matrix) - 1, x, 'u')
    ans = max(ans, get_count())

    state = reset_state()
    move(x, 0, 'r')
    ans = max(ans, get_count())

    state = reset_state()
    move(x, len(matrix) - 1, 'l')
    ans = max(ans, get_count())

print(ans)