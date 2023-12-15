file = open('input.txt')

def valid_interval(interval, check_start = True, check_end = True):
    if check_start:
        if interval[0] == '#':
            return False
        
        check_start = 1
    
    if check_end:
        if interval[-1] == '#':
            return False
        
        check_end = 1
    #if interval == '?.?##?':
    #    print(check_start, check_end)
    #    print(interval[check_start:len(interval) - check_end])
    #    print('.' not in interval[check_start:len(interval) - check_end])

    #print(interval[check_start:len(interval) - check_end], check_start, check_end)
    return '.' not in interval[check_start:len(interval) - check_end]

def can_place(remaining_interval, remaining_numbers):
    dots = remaining_interval.count('.')
    blocks = remaining_interval.count('#')
    undefs = remaining_interval.count('?')

    to_place = sum(remaining_numbers)

    if blocks + undefs < to_place:
        return False
    
    dots += (blocks + undefs) - to_place
    if dots < len(remaining_numbers) - 1:
        return False
    
    return True

def get_comb(interval, numbers):
    if len(numbers) == 0:
        return 0

    n = numbers[0]
    print(f'Checking {n}')

    start_index = 0
    while interval[start_index] == '.':
        start_index += 1
    end_index = start_index + n
    
    #print(interval)
    #debug = ' ' * len(interval)
    #debug = list(debug)
    #debug[start_index] = '^'
    #debug[end_index - 1] = '^'
    #print(''.join(debug))

    cont = 0
    while end_index <= len(interval) and can_place(interval[end_index + 1:], numbers[1:]):
        print(interval)
        debug = ' ' * len(interval)
        debug = list(debug)
        debug[start_index] = '^'
        debug[end_index - 1] = '^'
        print(''.join(debug))

        real_start = start_index - 1 if start_index > 0 else start_index
        real_end = end_index + 1 if end_index < len(interval) else end_index

        #print(real_start, real_end)
        #print(interval[real_start:real_end], valid_interval(interval[real_start:real_end], real_start != start_index, real_end != end_index))

        if valid_interval(interval[real_start:real_end], real_start != start_index, real_end != end_index):
            #cont += 1
            if len(numbers) > 1:
                cont += get_comb(interval[end_index + 1:], numbers[1:])
            else:
                if interval[end_index:].count('#') == 0:
                    cont += 1

        if interval[start_index] == '#':
            break

        start_index += 1
        end_index += 1

    print(f'End checking {n}')

    return cont

ans = 0
for line in file.readlines():
    line = line.strip()

    [interval, numbers] = line.split(' ')
    numbers = list(map(lambda n: int(n), numbers.split(',')))

    x = get_comb(interval, numbers)
    print(x)
    ans += x

print(ans)