file = open('input.txt')

times = list(map(lambda n: int(n.strip()), list(filter(lambda x: x != '', file.readline().split(':')[1].split(' ')))))
distances = list(map(lambda n: int(n.strip()), list(filter(lambda x: x != '', file.readline().split(':')[1].split(' ')))))

ans = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    minn = 0
    maxx = time

    while True:
        if ((time - minn) * minn) > distance:
            break
        minn += 1

    while True:
        if ((time - maxx) * maxx) > distance:
            break
        maxx -= 1

    ans *= (maxx - minn + 1)

print(ans)