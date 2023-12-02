file = open("input.txt")

str_monkeys = file.read().split("\n\n")

monkeys = {}
counter = {}
divisors = []

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
    divisors.append(int(x[3].split(" ")[5]))
    monkey["true_case"] = x[4].split(" ")[9]
    monkey["false_case"] = x[5].split(" ")[9]

    id = x[0].split(" ")[1].replace(":", "")
    
    monkeys[id] = monkey
    counter[id] = 0

big_number = 1
for d in divisors:
    big_number *= d

for _ in range(10000):
    if _ % 100 == 0:
        print(_)

    for monkey_i in monkeys:
        monkey = monkeys[monkey_i]
        counter[monkey_i] += len(monkey["start_items"])

        for item in monkey["start_items"]:
            op = monkey["operation"]
            op = op.replace("old", str(item))

            op = op.split(" ")
            if op[1] == "*":
                new_val = int(op[0]) * int(op[2])
            else:
                new_val = int(op[0]) + int(op[2])

            if new_val >= big_number:
                new_val = new_val % big_number

            if new_val % monkey["division_test"] == 0:
                monkeys[monkey["true_case"]]["start_items"].append(new_val)
            else:
                monkeys[monkey["false_case"]]["start_items"].append(new_val)

        monkey["start_items"] = []

ans = list(counter.values())
ans.sort(reverse=True)
print(ans[0] * ans[1])