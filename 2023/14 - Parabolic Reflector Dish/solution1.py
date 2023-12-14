file = open('input.txt')

matrix = []
last_block = []
row = 0
for line in file.readlines():
    line = line.strip()
    matrix.append([c for c in line])

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

ans = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        cell = matrix[i][j]

        if cell == 'O':
            ans += (len(matrix) - i)

print(ans)