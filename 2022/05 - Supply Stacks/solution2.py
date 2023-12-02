file = open("input.txt")
lines = file.read().split('\n')

dp = {
    1: "FCJPHTW",
    2: "GRVFZJBH",
    3: "HPTR",
    4: "ZSNPHT",
    5: "NVFZHJCD",
    6: "PMGFWDZ",
    7: "MVZWSJDP",
    8: "NDS",
    9: "DZSFM",
}

for line in lines:
    if line == "":
        continue

    temp = line.split(' ')
    q = int(temp[1])
    s = int(temp[3])
    e = int(temp[5])

    tomove = dp[s][len(dp[s]) - q:]
    dp[s] = dp[s][:len(dp[s]) - q]
    dp[e] += tomove

ans = ""
for i in range(1, 10):
    ans += dp[i][-1]

print(ans)