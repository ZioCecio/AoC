import functools
import operator

file = open("first.txt")
lines = file.read()
lines = lines.split('\n')

dp = []
temp = 0

for line in lines:
    if line == "":
        dp.append(temp)
        temp = 0
    else:
        temp += int(line)
    
dp.sort(reverse = True)
ans = functools.reduce(operator.add, dp[0:3])
print(ans)