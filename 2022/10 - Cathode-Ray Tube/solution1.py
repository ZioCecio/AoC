file = open("input.txt")

lines = file.read().split("\n")
lines.reverse()

register = 1
ans = 0

last = ""
for i in range(1, 221):
    if (i - 20 >= 0) and (i - 20) % 40 == 0:
        ans += (register * i)

    if last == "":
        inst = lines.pop()

        if inst.startswith("a"):
            last = inst

    else:
        n = int(last.split(" ")[1])
        register += n
        last = ""

print(ans)