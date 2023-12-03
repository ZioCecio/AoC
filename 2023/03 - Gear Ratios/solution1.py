file = open('input.txt')

symbols = {}
numbers = {}

line_index = 0
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
        elif c != '.':
            symbols[line_index].append(x)
            action = 2
        
        if action != 1 and len(num) > 0:
            numbers[line_index].append([int(num), (x - len(num), x - 1)])
            num = ''

    if len(num) > 0:
        numbers[line_index].append([int(num), (x - len(num), x - 1)])

    line_index += 1

ans = 0
for i in range(len(numbers)):
    for num in numbers[i]:
        for j in range(max(0, i - 1), min(line_index - 1, i + 1) + 1):
            
            added = False
            symbols_to_check = symbols[j]
            for symbol_pos in symbols_to_check:
                if symbol_pos >= num[1][0] - 1 and symbol_pos <= num[1][1] + 1:
                    added = True
                    ans += num[0]
                    break

            if added:
                break

print(ans)