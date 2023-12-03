file = open('input.txt')

symbols = {}
numbers = {}

line_index = 0
gear_id = 0
gear_parts = {}
for line in file.readlines():
    chars = line.strip()
    
    symbols[line_index] = []
    numbers[line_index] = []
    num = ''
    for x in range(len(chars)):
        c = chars[x]

        action = 0
        if c.isdigit():
            num += c
            action = 1
        elif c == '*':
            gear_parts[gear_id] = []
            symbols[line_index].append([x, gear_id])
            gear_id += 1
            action = 2
        
        if action != 1 and len(num) > 0:
            numbers[line_index].append([int(num), (x - len(num), x - 1)])
            num = ''

    if len(num) > 0:
        numbers[line_index].append([int(num), (x - len(num), x - 1)])

    line_index += 1

for i in range(len(numbers)):
    for num in numbers[i]:
        for j in range(max(0, i - 1), min(line_index - 1, i + 1) + 1):
            
            added = False
            symbols_to_check = symbols[j]
            for symbol_pos in symbols_to_check:
                if symbol_pos[0] >= num[1][0] - 1 and symbol_pos[0] <= num[1][1] + 1:
                    added = True
                    gear_parts[symbol_pos[1]].append(num[0])
                    break

            if added:
                break

ans = 0
for x in gear_parts:
    parts = gear_parts[x]

    if len(parts) == 2:
        ans += (parts[0] * parts[1])

print(ans)