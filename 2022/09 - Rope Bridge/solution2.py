def follow(head, tail):
    if head == tail:
        return

    if abs(head[0] - tail[0]) >= 2 and abs(head[1] - tail[1]) >= 2:
        if head[0] > tail[0]:
            tail[0] += 1
        else:
            tail[0] -= 1

        if head[1] > tail[1]:
            tail[1] += 1
        else:
            tail[1] -= 1
    elif head[0] - tail[0] >= 2:
        tail[0] += 1
        tail[1] = head[1]
    elif head[1] - tail[1] >= 2:
        tail[0] = head[0]
        tail[1] += 1
    elif head[0] - tail[0] <= -2:
        tail[0] -= 1
        tail[1] = head[1]
    elif head[1] - tail[1] <= -2:
        tail[0] = head[0]
        tail[1] -= 1

def draw():
    m = []
    for i in range(25):
        m.append([])
        for j in range(25):
            m[i].append('.')

    for i in range(len(nodes)):
        node = nodes[i]
        m[node[0]][node[1]] = i

    print()
    for x in m:
        print(x)
    print()

file = open("input.txt")

lines = file.read().split("\n")

nodes = []
for _ in range(10):
    nodes.append([0, 0])

positions = {}

for line in lines:
    print(line)
    d = line.split(" ")[0]
    t = int(line.split(" ")[1])

    if d == "U":
        for i in range(t):
            nodes[0][0] += 1
            for j in range(1, 10):
                follow(nodes[j - 1], nodes[j])

            positions[f"{nodes[9][0]}{nodes[9][1]}"] = 1
            print(nodes)

    if d == "D":
        for i in range(t):
            nodes[0][0] -= 1
            for j in range(1, 10):
                follow(nodes[j - 1], nodes[j])

            positions[f"{nodes[9][0]}{nodes[9][1]}"] = 1
            print(nodes)

    if d == "R":
        for i in range(t):
            nodes[0][1] += 1
            for j in range(1, 10):
                follow(nodes[j - 1], nodes[j])

            positions[f"{nodes[9][0]}{nodes[9][1]}"] = 1
            print(nodes)

    if d == "L":
        for i in range(t):
            nodes[0][1] -= 1
            for j in range(1, 10):
                follow(nodes[j - 1], nodes[j])

            positions[f"{nodes[9][0]}{nodes[9][1]}"] = 1
            print(nodes)

    print()

print(len(positions.keys()))