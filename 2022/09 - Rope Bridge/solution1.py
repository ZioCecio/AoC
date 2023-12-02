def up():
    if hp[0] == tp[0]:
        hp[0] += 1
        return

    hp[0] += 1

    if hp[0] == tp[0]:
        return

    if hp[1] == tp[1]:
        tp[0] += 1
    else:
        tp[0] += 1
        tp[1] = hp[1]


def down():
    if hp[0] == tp[0]:
        hp[0] -= 1
        return

    hp[0] -= 1

    if hp[0] == tp[0]:
        return

    if hp[1] == tp[1]:
        tp[0] -= 1
    else:
        tp[0] -= 1
        tp[1] = hp[1]

def right():
    if hp[1] == tp[1]:
        hp[1] += 1
        return

    hp[1] += 1

    if hp[1] == tp[1]:
        return

    if hp[0] == tp[0]:
        tp[1] += 1
    else:
        tp[1] += 1
        tp[0] = hp[0]

def left():
    if hp[1] == tp[1]:
        hp[1] -= 1
        return

    hp[1] -= 1

    if hp[1] == tp[1]:
        return

    if hp[0] == tp[0]:
        tp[1] -= 1
    else:
        tp[1] -= 1
        tp[0] = hp[0]

file = open("input.txt")

lines = file.read().split("\n")

hp = [0, 0]
tp = [0, 0]

positions = {}

for line in lines:
    d = line.split(" ")[0]
    t = int(line.split(" ")[1])

    if d == "U":
        for i in range(t):
            up()
            positions[f"{tp[0]}{tp[1]}"] = 1
            print(tp)

    if d == "D":
        for i in range(t):
            down()
            positions[f"{tp[0]}{tp[1]}"] = 1
            print(tp)

    if d == "R":
        for i in range(t):
            right()
            positions[f"{tp[0]}{tp[1]}"] = 1
            print(tp)

    if d == "L":
        for i in range(t):
            left()
            positions[f"{tp[0]}{tp[1]}"] = 1
            print(tp)

print(len(positions.keys()))