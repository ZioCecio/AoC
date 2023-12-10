file = open('input.txt')

numbers = []
for line in file.readlines():
    numbers.append(list(map(lambda n : int(n), line.split(' '))))

def resolve_numbers(num):
    all_zeros = True

    new_num = []
    for i in range(1, len(num)):
        x = num[i] - num[i - 1]
        new_num.append(x)

        if x != 0:
            all_zeros = False

    if all_zeros:
        return num[0]
    
    return num[0] - resolve_numbers(new_num)

ans = 0
for num in numbers:
    ans += resolve_numbers(num)
    
print(ans)