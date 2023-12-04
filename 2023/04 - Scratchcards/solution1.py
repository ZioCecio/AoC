file = open('input.txt')

ans = 0
for line in file.readlines():
    [_, numbers] = line.strip().split(':')

    [card_numbers, winning_numbers] = numbers.split('|')
    
    card_numbers = list(filter(lambda n : n.isdigit(), card_numbers.strip().split(' ')))
    winning_numbers = list(filter(lambda n : n.isdigit(), winning_numbers.strip().split(' ')))

    win_cont = 0
    for card_number in card_numbers:
        if card_number in winning_numbers:
            win_cont += 1

    if win_cont > 0:
        ans += (2 ** (win_cont - 1))

print(ans)