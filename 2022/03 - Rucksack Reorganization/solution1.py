file = open("input.txt")
lines = file.read().split('\n')

ans = 0
for line in lines:
    if line == "":
        continue

    half = len(line) // 2
    first = line[:half]
    second = line[half:]

    for c in first:
        if c in second:
            if ord(c) > 90:
                ans += (ord(c) - ord('a') + 1)
            else:
                ans += (ord(c) - ord('A') + 27)

            break
            

print(ans)