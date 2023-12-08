import math

file = open('input.txt')

sequence = file.readline().strip()
file.readline()

tree = {}
current_nodes = []
for line in file.readlines():
    [parent, children] = line.split(' = ')
    children = children.strip()

    child_a = children[1:4]
    child_b = children[6:-1]

    tree[parent] = (child_a, child_b)

    if parent.endswith('A'):
        current_nodes.append(parent)

fastes_steps = {}
for current_node in current_nodes:
    s_i = 0
    steps = 0
    start_node = current_node
    while current_node[-1] != 'Z':
        move = sequence[s_i]

        if move == 'L':
            current_node = tree[current_node][0]
        else:
            current_node = tree[current_node][1]

        steps += 1
        s_i = (s_i + 1) % len(sequence)

    fastes_steps[start_node] = (steps, current_node)

numbers = []
for c in fastes_steps:
    numbers.append(fastes_steps[c][0])

ans = math.lcm(*numbers)
print(ans)