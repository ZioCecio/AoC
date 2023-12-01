file = open('input.txt')

ans = 0
for line in file.readlines():
    digits = list(filter(lambda c: c.isdigit(), list(line)))
    
    if len(digits) == 0:
        continue

    ans += int(f'{digits[0]}{digits[-1]}')
        
print(ans)