file = open('input.txt')

def get_sol(mat):
    for i in range(len(mat) - 1):
        if mat[i] == mat[i + 1]:
            j = 0

            while i - j >= 0 and i + j + 1 < len(mat):
                if mat[i - j] != mat[i + j + 1]:
                    break
                j += 1

            if i - j == -1 or (i + j + 1) == len(mat):
                return i + 1
    return 0

def get_rotated_matrix(matrix):
    new_matrix = [''] * len(matrix[0])

    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            new_matrix[j] += matrix[i][j]

    return new_matrix

matrix = []
ans = 0
for line in file.readlines():
    line = line.strip()

    if line != '':
        matrix.append(line)
        continue

    ans += (100 * get_sol(matrix))
    new_matrix = get_rotated_matrix(matrix)
    ans += get_sol(new_matrix)

    matrix = []

print(ans)