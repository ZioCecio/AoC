file = open('input.txt')

time = int(file.readline().split(':')[1].replace(' ', ''))
distance = int(file.readline().split(':')[1].replace(' ', ''))

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

    

print(maxx - minn + 1)