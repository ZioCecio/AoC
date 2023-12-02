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
                return False
            elif a < b:
                return True
        elif type(a) == list and type(b) != list:
            temp = are_right(a, [b])
        elif type(a) != list and type(b) == list:
            temp = are_right([a], b)
        else:
            temp = are_right(a, b)

        if temp != None:
            return temp

    if len(list1) < len(list2):
        return True
    elif len(list1) > len(list2):
        return False

file = open("input.txt")
lines = file.read().split("\n")

ans = 0
t = 1
for i in range(0, len(lines), 3):
    (list1, _) = get_list(lines[i], 0)
    (list2, _) = get_list(lines[i + 1], 0)

    res = are_right(list1, list2)
    print(f"{t}: {res}")

    if res == True:
        ans += t

    t += 1

print(ans)