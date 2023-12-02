file = open("input.txt")

lines = file.read().split("\n")
lines.reverse()

register = 1
R = 6
C = 40

display = []
row = -1

last = ""
for i in range(240):
    if i % 40 == 0:
        row += 1
        display.append([])

    c = int(i % 40)
    if c >= (register - 1) and c <= (register + 1):
        display[row].append("#")
    else:
        display[row].append(".")

    if last == "":
        inst = lines.pop()

        if inst.startswith("a"):
            last = inst

    else:
        n = int(last.split(" ")[1])
        register += n
        last = ""

for x in display:
    print(" ".join(x))