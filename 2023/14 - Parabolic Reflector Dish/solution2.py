from hashlib import sha1

file = open('input.txt')

def tilt_matrix(matrix):
    last_block = []
    row = 0
    for line in matrix:
        if last_block == []:
            last_block = [-1] * len(line)

        for i in range(len(line)):
            cell = line[i]

            if cell == '#':
                last_block[i] = row
            elif cell == 'O':
                new_pos = last_block[i] + 1
                last_block[i] += 1
                matrix[row][i] = '.'
                matrix[new_pos][i] = 'O'

        row += 1

    return matrix

def rotate_matrix(matrix):
    new_matrix = [[''] * len(matrix) for _ in range(len(matrix[0]))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            r = j
            c = len(matrix) - i - 1

            #print(f'(i, j) = ({i}, {j}); (r, c) = ({r}, {c})')

            new_matrix[r][c] = matrix[i][j]

    return new_matrix

def get_hash(matrix):
    state = ''
    for x in matrix:
        state += ''.join(x)
    return sha1(state.encode()).hexdigest()

matrix = []
for line in file.readlines():
    line = line.strip()
    matrix.append([c for c in line])

cycle_count = 1000000000
saved_states = {}
for i in range(cycle_count):
    #print(i + 1)
    for _ in range(4):
        matrix = tilt_matrix(matrix)
        matrix = rotate_matrix(matrix)

    id = get_hash(matrix)
    if id in saved_states:
        print(len(saved_states))
        break

    saved_states[id] = 0
    #for x in matrix:
    #    print(x)
    
    #print()

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        cell = matrix[i][j]

        if cell == 'O':
            ans += (len(matrix) - i)

print(ans)