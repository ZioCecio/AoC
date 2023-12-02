file = open("input.txt")
lines = file.read().split('\n')

ans = 0
for line in lines:
    if line == "":
        continue

    x = line.split(" ")

    os = x[0][0]
    ms = x[1][0]

    temp = (ord(ms) - ord('X') + 1)

    if ord(os) == (ord(ms) - 23):
        temp += 3

    if os == "A" and ms == "Y":
        temp += 6

    if os == "B" and ms == "Z":
        temp += 6

    if os == "C" and ms == "X":
        temp += 6

    ans += temp

print(ans)