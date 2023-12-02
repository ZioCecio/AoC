def helper(node):
    for c in node["children"]:
        node["size"] += helper(c)

    return node["size"]

def get_ans(node):
    ans = 0

    if node["size"] <= 100000:
        ans += node["size"]

    for c in node["children"]:
        ans += get_ans(c)

    return ans

def main():
    file = open("input.txt")

    lines = file.read().split("\n")
    L = len(lines)

    tree = {
        "dir": "/",
        "size": 0,
        "parent": None,
        "children": []
    }
    current_node = tree
    for i in range(L):
        line = lines[i]

        if line.startswith("$"):
            if ".." in line:
                current_node = current_node["parent"]

            elif "cd" in line:
                name = line.split(" ")[2]

                for c in current_node["children"]:
                    if c["dir"] == name:
                        current_node = c
                        break
                
            else:
                i += 1
                while i < L and not lines[i].startswith("$"):
                    if lines[i].split(" ")[0] == "dir":
                        current_node["children"].append({
                            "dir": lines[i].split(" ")[1],
                            "size": 0,
                            "parent": current_node,
                            "children": []
                        })
                    else:
                        current_node["size"] += int(lines[i].split(" ")[0])

                    i += 1

                i -= 1

    helper(tree)
    ans = get_ans(tree)
    print(ans)

main()