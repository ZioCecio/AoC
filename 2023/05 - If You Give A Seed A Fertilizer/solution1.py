file = open('input.txt')

seeds = list(map(lambda n : int(n), file.readline().split(':')[1].strip().split(' ')))
file.readline()

maps = {}
is_new_map = True
last_map_key = ''

for line in file.readlines():
    line = line.strip()
    if is_new_map:
        is_new_map = False
        
        last_map_key = line[:-1]
        maps[last_map_key] = []
        
        continue

    if line == '':
        is_new_map = True
        continue

    ranges = list(map(lambda n : int(n), line.split(' ')))
    maps[last_map_key].append(ranges)

transformations = {}
for seed in seeds:
    transformations[seed] = seed

    for map_key in maps:
        for ranges in maps[map_key]:
            [dest, source, length] = ranges

            if transformations[seed] >= source and transformations[seed] < (source + length):
                transformations[seed] = dest + (transformations[seed] - source)
                break

ans = float('inf')
for seed in transformations:
    ans = min(ans, transformations[seed])

print(ans)