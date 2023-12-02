file = open("input.txt")
lines = file.read().split('\n')

ans = 0
for line in lines:
    if line == "":
        continue

    x = line.split(" ")

    os = chr(ord(x[0][0]) + 23)
    ms = x[1][0]

    temp = 0
    signs = ["X", "Y", "Z"]
    if ms == "X":
        ms = signs[signs.index(os) - 1]
    elif ms == "Y":
        temp = 3
        ms = signs[signs.index(os)]
    else:
        temp = 6
        ms = signs[(signs.index(os) + 1) % 3]

    temp += (ord(ms) - ord('X') + 1)

    ans += temp

print(ans)