file = open('input.txt')

sequence = file.readline().strip()
file.readline()

tree = {}
for line in file.readlines():
    [parent, children] = line.split(' = ')
    children = children.strip()

    child_a = children[1:4]
    child_b = children[6:-1]

    tree[parent] = (child_a, child_b)

ans = 0
s_i = 0
current_node = 'AAA'
while current_node != 'ZZZ':
    move = sequence[s_i]

    if move == 'L':
        current_node = tree[current_node][0]
    else:
        current_node = tree[current_node][1]

    ans += 1
    s_i = (s_i + 1) % len(sequence)

print(ans)