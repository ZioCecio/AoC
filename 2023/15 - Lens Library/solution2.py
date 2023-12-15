file = open('input.txt')

def get_hash(string):
    current_value = 0

    for c in string:
        if c == '\n':
            continue

        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256

    return current_value


text = file.read()
activation_sequence = text.split(',')

boxes = {}
for x in activation_sequence:
    if '-' in x:
        raw_position = x.split('-')[0]    
        position = get_hash(raw_position)
        
        if position not in boxes:
            boxes[position] = []

        boxes[position] = list(filter(lambda lens: lens[0] != raw_position, boxes[position]))

    else:
        [raw_position, focal] = x.split('=')
        position = get_hash(raw_position)
        focal = int(focal)

        if position not in boxes:
            boxes[position] = []
        
        updated = False
        for lens in boxes[position]:
            if lens[0] == raw_position:
                lens[1] = focal
                updated = True
                break
        
        if not updated:
            boxes[position].append([raw_position, focal])

ans = 0
for key in boxes:
    box = boxes[key]
    for i in range(len(box)):
        lens = box[i]

        ans += ((key + 1) * (i + 1) * lens[1])

print(ans)