file = open("input.txt")
lines = file.read().split('\n')

ans = 0
for i in range(0, len(lines) - 1, 3):
    first = lines[i]
    second = lines[i + 1]
    third = lines[i + 2]

    for c in first:
        if c in second and c in third:
            if ord(c) > 90:
                ans += (ord(c) - ord('a') + 1)
            else:
                ans += (ord(c) - ord('A') + 27)

            break

print(ans)