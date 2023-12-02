def get_list(string, i):
    i += 1

    arr = []
    while i < len(string) and string[i] != ']':
        if string[i] == '[':
            (new_arr, new_i) = get_list(string, i)
            arr.append(new_arr)
            i = new_i + 1
        elif string[i] != ',':
            num = ""
            while string[i] >= '0' and string[i] <= '9':
                num += string[i]
                i += 1
            arr.append(int(num))
        else:
            i += 1
    
    return (arr, i)

def are_right(list1, list2):
    for i in range(min(len(list1), len(list2))):
        a = list1[i]
        b = list2[i]
        
        temp = None
        if type(a) != list and type(b) != list:
            if a > b:
                return -1
            elif a < b:
                return 1
        elif type(a) == list and type(b) != list:
            temp = are_right(a, [b])
        elif type(a) != list and type(b) == list:
            temp = are_right([a], b)
        else:
            temp = are_right(a, b)

        if temp != None:
            return temp

    if len(list1) < len(list2):
        return 1
    elif len(list1) > len(list2):
        return -1

file = open("input.txt")
lines = file.read().split("\n")

packets = []
for line in lines:
    if line == "":
        continue

    p = get_list(line, 0)[0]
    packets.append(p)

packets.append([[2]])
packets.append([[6]])

from functools import cmp_to_key
s = sorted(packets, key=cmp_to_key(are_right), reverse=True)

a = 0
b = 0
for i in range(len(s)):
    if s[i] == [[2]]:
        a = i + 1

    if s[i] == [[6]]:
        b = i + 1

print(a * b)