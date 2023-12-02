file = open("input.txt")

grid = []
dp = []
lines = file.read().split("\n")

for i in range(len(lines)):
    grid.append([])
    dp.append([])
    for c in lines[i]:
        grid[i].append(int(c))
        dp[i].append(False)

R = len(grid)
C = len(grid[0])

for i in range(1, R - 1):
    maxx = grid[i][0]
    for j in range(1, C - 1):
        if grid[i][j] > maxx:
            maxx = grid[i][j]
            dp[i][j] = True

for i in range(1, R - 1):
    maxx = grid[i][C - 1]
    for j in reversed(range(1, C - 1)):
        if grid[i][j] > maxx:
            maxx = grid[i][j]
            dp[i][j] = True

for j in range(1, C - 1):
    maxx = grid[0][j]
    for i in range(1, R - 1):
        if grid[i][j] > maxx:
            maxx = grid[i][j]
            dp[i][j] = True

for j in range(1, C - 1):
    maxx = grid[R - 1][j]
    for i in reversed(range(1, R - 1)):
        if grid[i][j] > maxx:
            maxx = grid[i][j]
            dp[i][j] = True

ans = (R * 2) + (C * 2) - 4
for i in range(1, R - 1):
    for j in range(1, C - 1):
        if dp[i][j] == True:
            ans += 1
