def add_rock(c1, c2):
    x1 = int(c1[1])
    y1 = int(c1[0])

    x2 = int(c2[1])
    y2 = int(c2[0])

    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        for i in range(a, b + 1):
            cave[x1][i] = 1
    elif y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for i in range(a, b + 1):
            cave[i][y1] = 1

def add_sand():
    i = 0
    j = 500

    while i < 299:
        cave[i][j] = 0
        if cave[i + 1][j] == 0:
            i += 1
        elif cave[i + 1][j - 1] == 0:
            i += 1
            j -= 1
        elif cave[i + 1][j + 1] == 0:
            i += 1
            j += 1
        else:
            cave[i][j] = 2
            return True
        
        cave[i][j] = 2

    return False

file = open("input.txt")
lines = file.read().split("\n")

cave = []
for i in range(300):
    cave.append([])

    for _ in range(1000):
        cave[i].append(0)

    
for line in lines:
    coord = line.split(" -> ")

    for i in range(len(coord) - 1):
        add_rock(coord[i].split(","), coord[i + 1].split(","))

ans = 0
while(add_sand()):
    ans += 1

print(ans)
