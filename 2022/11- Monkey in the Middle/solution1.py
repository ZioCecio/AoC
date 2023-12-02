file = open("input.txt")

str_monkeys = file.read().split("\n\n")

monkeys = {}
counter = {}

for x in str_monkeys:
    x = x.split("\n")

    monkey = {
        "start_items": []
    }

    for item in x[1].split(" ")[4:]:
        item = item.replace(",", "")
        
        monkey["start_items"].append(int(item))

    monkey["operation"] = " ".join(x[2].split(" ")[5:])
    monkey["division_test"] = int(x[3].split(" ")[5])
    monkey["true_case"] = x[4].split(" ")[9]
    monkey["false_case"] = x[5].split(" ")[9]

    id = x[0].split(" ")[1].replace(":", "")
    
    monkeys[id] = monkey
    counter[id] = 0

for _ in range(20):

    for monkey_i in monkeys:
        monkey = monkeys[monkey_i]
        counter[monkey_i] += len(monkey["start_items"])

        for item in monkey["start_items"]:
            op = monkey["operation"]
            op = op.replace("old", str(item))

            new_val = eval(op)
            new_val = int(new_val / 3)

            if new_val % monkey["division_test"] == 0:
                monkeys[monkey["true_case"]]["start_items"].append(new_val)
            else:
                monkeys[monkey["false_case"]]["start_items"].append(new_val)

        monkey["start_items"] = []

ans = list(counter.values())
ans.sort(reverse=True)
print(ans[0] * ans[1])