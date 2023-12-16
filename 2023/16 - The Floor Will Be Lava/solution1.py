file = open('input.txt')

matrix = []
state = []
for line in file.readlines():
    line = line.strip()
    matrix.append(list(line))
    state.append([['.', None]] * len(line))

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

import sys
sys.setrecursionlimit(3000)

move(0, 0, 'r')
ans = 0
for x in state:
    for y in x:
        ans += 1 if y[0] == '#' else 0

print(ans)