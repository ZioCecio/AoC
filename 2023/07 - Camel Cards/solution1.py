import functools

file = open('input.txt')

# 6: Five Of A Kind
# 5: Poker
# 4: Full House
# 3: Tris
# 2: Two Pair
# 1: One Pair
# 0: High Card
def get_hand_type(hand):
    types = {}

    for card in hand:
        if card not in types:
            types[card] = 1
        else:
            types[card] += 1
        
    n = len(types)
    if n == 1:
        return 6
    
    if n == 2:
        first_key = list(types.keys())[0]

        if types[first_key] == 4 or types[first_key] == 1:
            return 5
        else:
            return 4

    if n == 3:
        for key in types:
            occ = types[key]

            if occ == 3:
                return 3
            
        return 2

    if n == 4:
        return 1
    
    return 0

card_values = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}
def compare_hands(h1, h2):
    if h1['hand_type'] != h2['hand_type']:
        return h1['hand_type'] - h2['hand_type']
    
    for i in range(len(h1['hand'])):
        h1c = int(h1['hand'][i]) if h1['hand'][i].isdigit() else card_values[h1['hand'][i]]
        h2c = int(h2['hand'][i]) if h2['hand'][i].isdigit() else card_values[h2['hand'][i]]

        if h1c != h2c:
            return h1c - h2c
        
    return 0

        

cards = []
for line in file.readlines():
    [hand, bet] = line.strip().split(' ')
    hand_type = get_hand_type(hand)
    cards.append({ 'hand': hand, 'bet': int(bet), 'hand_type': hand_type })

cards = list(sorted(cards, key=functools.cmp_to_key(compare_hands)))

ans = 0
for i in range(len(cards)):
    ans += (cards[i]['bet'] * (i + 1))
print(ans)