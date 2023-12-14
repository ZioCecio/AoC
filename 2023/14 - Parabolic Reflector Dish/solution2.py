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

            new_matrix[r][c] = matrix[i][j]

    return new_matrix

def get_hash(matrix):
    state = ''
    for x in matrix:
        state += ''.join(x)
    return sha1(state.encode()).hexdigest()

def get_score(mat):
    score = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            cell = mat[i][j]

            if cell == 'O':
                score += (len(mat) - i)

    return score

matrix = []
for line in file.readlines():
    line = line.strip()
    matrix.append([c for c in line])

cycle_count = 1000000000

end_id = None
saved_states = {}
for i in range(cycle_count):
    force_exit = False

    for _ in range(4):
        matrix = tilt_matrix(matrix)
        matrix = rotate_matrix(matrix)

    id = get_hash(matrix)

    if id in saved_states:
        start_cycle = saved_states[id]
        cycle_length = len(saved_states) - start_cycle + 1
        cycle_count -= start_cycle

        end_all = start_cycle + (cycle_count % cycle_length)

        for key in saved_states:
            if saved_states[key] == end_all:
                end_id = key
                force_exit = True
                break

        break

    if force_exit:
        break

    saved_states[id] = len(saved_states) + 1

while id != end_id:
    for _ in range(4):
        matrix = tilt_matrix(matrix)
        matrix = rotate_matrix(matrix)

    id = get_hash(matrix)

ans = get_score(matrix)
print(ans)