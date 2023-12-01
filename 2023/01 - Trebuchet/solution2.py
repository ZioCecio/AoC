import re

file = open('input.txt')

spelled_numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

ans = 0
for line in file.readlines():
    regex = f'{"|".join(spelled_numbers.keys())}|\d'
    
    iters = re.finditer(f'(?=({regex}))', line.strip())
    digits = [iter.groups(0)[0] for iter in iters]
    digits = list(map(lambda d: d if d.isdigit() else spelled_numbers[d], digits))
    

    if len(digits) == 0:
        continue
    
    ans += int(f'{digits[0]}{digits[-1]}')

print(ans)