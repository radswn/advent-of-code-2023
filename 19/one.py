with open("19/input.txt") as f:
    lines = f.read().split("\n")


workflows_raw = []
workflows = {}
parts = []
current = workflows_raw

for l in lines:
    if l == "":
        current = parts
        continue

    current.append(l)

for w in workflows_raw:
    w_name, rest = w.split("{")
    workflows[w_name] = [
        x for x in rest[:-1].split(",")
    ]
    processed_rules = []
    for rule in workflows[w_name]:
        colon_idx = rule.find(":")
        if colon_idx == -1:
            processed_rules.append(rule)
        else:
            processed_rules.append((rule[0], rule[1], int(rule[2:colon_idx]), rule[colon_idx + 1:]))
    workflows[w_name] = processed_rules

total = 0

for part in parts:
    x, m, a, s = [int(p[2:]) for p in part[1:-1].split(",")]
    part_values = {"x": x, "m": m, "a": a, "s": s}
    wflow = "in"
    
    while wflow not in ("R", "A"):
        for rule in workflows[wflow]:
            if type(rule) == str:
                wflow = rule
                continue
            else:
                attr, sign, value, dest_wflow = rule
                if sign == "<" and part_values[attr] < value: wflow = dest_wflow; break
                elif sign == ">" and part_values[attr] > value: wflow = dest_wflow; break
    
    if wflow == "A": total += sum(part_values.values())

print(total)
