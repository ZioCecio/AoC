file = open("input.txt")
lines = file.read().split('\n')

ans = 0
for line in lines:
    if line == "":
        continue

    pair = line.split(',')

    f = pair[0]
    s = pair[1]

    f1 = int(f.split('-')[0])
    f2 = int(f.split('-')[1])

    s1 = int(s.split('-')[0])
    s2 = int(s.split('-')[1])

    if f1 >= s1 and f1 <= s2:
        ans += 1
    elif f2 >= s1 and f2 <= s2:
        ans += 1
    elif s1 >= f1 and s1 <= f2:
        ans += 1
    elif s2 >= f1 and s2 <= f2:
        ans += 1    

print(ans)