file = open('input.txt')

galaxies = {}
saved_map = []

row_number = 0
for line in file.readlines():
    line = line.strip()
    saved_map.append(line)

    if '#' not in line:
        row_number += 1
    else:
        positions = [pos for pos, char in enumerate(line) if char == '#']

        for position in positions:
            galaxy_id = len(galaxies) + 1
            galaxies[galaxy_id] = [row_number, position]

    row_number += 1

to_sums = {}
for j in range(len(saved_map[0])):
    empty_col = True

    for i in range(len(saved_map)):
        if saved_map[i][j] == '#':
            empty_col = False
            break

    if empty_col:
        for x in galaxies:
            galaxy = galaxies[x]

            if galaxy[1] > j:
                if x not in to_sums:
                    to_sums[x] = 0

                to_sums[x] += 1

for x in to_sums:
    galaxies[x][1] += to_sums[x]

def get_distance(a, b):
    g_a = galaxies[a]
    g_b = galaxies[b]

    minn = min(abs(g_a[0] - g_b[0]), abs(g_a[1] - g_b[1]))
    maxx = max(abs(g_a[0] - g_b[0]), abs(g_a[1] - g_b[1])) - minn

    return minn * 2 + maxx

ans = 0
for i in range(len(galaxies) - 1):
    for j in range(i + 1, len(galaxies)):
        ans += get_distance(i + 1, j + 1)

print(ans)