import sys 

def explore(pos):
    [i, j] = pos

    if j < (C - 1) and steps[i][j + 1] > (steps[i][j] + 1) and (grid[i][j] - grid[i][j + 1]) >= -1:
        steps[i][j + 1] = steps[i][j] + 1
        explore([i, j + 1])

    if i < (R - 1) and steps[i + 1][j] > (steps[i][j] + 1) and (grid[i][j] - grid[i + 1][j]) >= -1:
        steps[i + 1][j] = steps[i][j] + 1
        explore([i + 1, j])

    if i > 0 and steps[i - 1][j] > (steps[i][j] + 1) and (grid[i][j] - grid[i - 1][j]) >= -1:
        steps[i - 1][j] = steps[i][j] + 1
        explore([i - 1, j])

    if j > 0 and steps[i][j - 1] > (steps[i][j] + 1) and (grid[i][j] - grid[i][j - 1]) >= -1:
        steps[i][j - 1] = steps[i][j] + 1
        explore([i, j - 1])


file = open("input.txt")

lines = file.read().split("\n")

grid = []
steps = []

start = [0, 0]
stop = [0, 0]

for i in range(len(lines)):
    grid.append([])
    steps.append([])

    for j in range(len(lines[i])):
        c = lines[i][j]

        if c == "S":
            start = [i, j]
            grid[i].append(0)
            steps[i].append(0)
        elif c == "E":
            stop = [i, j]
            grid[i].append(25)
            steps[i].append(float("inf"))
        else:
            grid[i].append(ord(c) - ord('a'))
            steps[i].append(float("inf"))

R = len(grid)
C = len(grid[0])

print(R, C)

sys.setrecursionlimit(3000)
explore(start)

for x in steps:
    print(x)

print(steps[stop[0]][stop[1]])