def get_coord(line):
    line = line.split(":")

    first = line[0].split(",")
    second = line[1].split(",")

    xs = int(first[0].split("=")[1])
    ys = int(first[1].split("=")[1])

    xb = int(second[0].split("=")[1])
    yb = int(second[1].split("=")[1])

    return ((xs, ys), (xb, yb))

def get_distance(sensor, beacon):
    (xs, ys) = sensor
    (xb, yb) = beacon

    return abs(xs - xb) + abs(ys - yb)

Y = 2000000
def add_in_line(s, b):
    dist = get_distance(s, b)
    ys = s[1]

    
    if Y < ys - dist or Y > ys + dist:
        return

    ydist = abs(s[1] - Y)
    halfrange = abs(dist - ydist)

    for i in range(s[0] - halfrange, s[0] + halfrange + 1):
        line_to_check.add(i)
    

file = open("input.txt")
lines = file.read().split("\n")

line_to_check = set()
to_remove = 0
dp = set()

for line in lines:
    (s, b) = get_coord(line)
    add_in_line(s, b)

    if b[1] == Y and b not in dp:
        dp.add(b)
        to_remove += 1

print(len(line_to_check) - to_remove)