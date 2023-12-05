file = open('input.txt')

seeds = []
seeds_ranges = list(map(lambda n : int(n), file.readline().split(':')[1].strip().split(' ')))
for i in range(0, len(seeds_ranges), 2):
    seeds.append([seeds_ranges[i], seeds_ranges[i] + seeds_ranges[i + 1], False])

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


def split_interval(interval_to_split, interval_target):
    [to_split_start, to_split_length, _] = interval_to_split
    [target_start, target_length] = interval_target

    to_split_end = to_split_start + to_split_length - 1
    target_end = target_start + target_length - 1

    if to_split_end < target_start:
        return [interval_to_split, None, None]
    
    if to_split_start > target_end:
        return [None, None, interval_to_split]
    
    if to_split_start >= target_start and to_split_end <= target_end:
        return [None, interval_to_split, None]

    if to_split_start < target_start and to_split_end <= target_end:
        first = [to_split_start, target_start - to_split_start]
        second = [target_start, to_split_end - target_start + 1]
        return [first, second, None]
    
    if to_split_start >= target_start and to_split_end > target_end:
        second = [to_split_start, target_end - to_split_start + 1]
        third = [target_end + 1, to_split_end - target_end]
        return [None, second, third]
    
    first = [to_split_start, target_start - to_split_start]
    second = interval_target
    third = [target_end + 1, to_split_end - target_end]
    return [first, second, third]

#print(split_interval([1, 10], [4, 4]))

for map_key in maps:
    transforms = []
    for ranges in maps[map_key]:
        [dest_start, source_start, length] = ranges
        source_end = source_start + length - 1
        
        for seed in seeds:
            target = [source_start, length]

            [first, second, third] = split_interval(seed, target)
            
            if second != None:
                if first != None:
                    seeds.append([first[0], first[1], False])

                if third != None:
                    seeds.append([third[0], third[1], False])
                
                transforms.append([dest_start + (second[0] - source_start), second[1], False])
                seed[2] = True
            
            

        seeds = list(filter(lambda s : s[2] != None and not s[2], seeds))

    seeds += transforms

ans = float('inf')
for x in seeds:
    ans = min(ans, x[0])

print(ans)
print(seeds)