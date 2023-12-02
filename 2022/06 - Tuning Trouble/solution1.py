file = open('input.txt')
stream = file.read()

for i in range(len(stream) - 4):
    dp = {}
    equal = False

    for j in range(i, i + 4):
        if stream[j] not in dp.keys():
            dp[stream[j]] = 1
        else:
            equal = True
            break

    if equal == False:
        print(i + 4)
        break
    