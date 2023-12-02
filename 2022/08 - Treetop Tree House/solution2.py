def get_res(i, j):
    ans = 1
    val = grid[i][j]

    t = 0
    for x in reversed(range(0, i)):
        t += 1

        if grid[x][j] >= val:
            break
    
    ans *= t
    t = 0
    for x in range(i + 1, R):
        t += 1

        if grid[x][j] >= val:
            break

    ans *= t
    t = 0
    for x in reversed(range(0, j)):
        t += 1

        if grid[i][x] >= val:
            break

    ans *= t
    t = 0
    for x in range(j + 1, C):
        t += 1

        if grid[i][x] >= val:
            break

    ans *= t
    return ans

file = open("input.txt")

grid = []
lines = file.read().split("\n")

for i in range(len(lines)):
    grid.append([])
    for c in lines[i]:
        grid[i].append(int(c))

R = len(grid)
C = len(grid[0])

ans = 0
for i in range(1, R - 1):
    for j in range(1, C - 1):
        ans = max(ans, get_res(i, j))

print(ans)