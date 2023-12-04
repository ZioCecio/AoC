file = open('input.txt')

row = 1
saved_wins = {}
copies = {}
for line in file.readlines():
    [_, numbers] = line.strip().split(':')

    [card_numbers, winning_numbers] = numbers.split('|')
    
    card_numbers = list(filter(lambda n : n.isdigit(), card_numbers.strip().split(' ')))
    winning_numbers = list(filter(lambda n : n.isdigit(), winning_numbers.strip().split(' ')))

    saved_wins[row] = 0
    copies[row] = 1
    for card_number in card_numbers:
        if card_number in winning_numbers:
            saved_wins[row] += 1
    row += 1

for k in saved_wins:
    x = saved_wins[k]

    for i in range(k + 1, min(k + x + 1, len(copies) + 1)):
        copies[i] += (copies[k])

ans = 0
for k in copies:
    ans += copies[k]

print(ans)