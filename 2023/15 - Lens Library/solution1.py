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

ans = 0
for x in activation_sequence:
    ans += get_hash(x)

print(ans)