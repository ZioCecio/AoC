file = open("first.txt")
lines = file.read()
lines = lines.split('\n')

ans = 0
temp = 0

for line in lines:
    if line == "":
        ans = max(ans, temp)
        temp = 0
    else:
        temp += int(line)
    
ans = max(ans, temp)
print(ans)