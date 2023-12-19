with open("19/input.txt") as f:
    lines = f.read().split("\n")

workflows = {}

for w in lines:
    if w == "":
        break

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

valid_ranges = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
ranges_per_wflow = {w: [] for w in workflows}
ranges_per_wflow["A"] = []
ranges_per_wflow["R"] = []
ranges_per_wflow["in"].append(valid_ranges)

while True:
    nonempty_workflows = {k: v for k, v in ranges_per_wflow.items() if k not in ("A", "R") and v != []}
    if not len(nonempty_workflows): break

    for wflow in nonempty_workflows:
        while len(nonempty_workflows[wflow]):
            incl_ranges = nonempty_workflows[wflow].pop(0)

            for rule in workflows[wflow]:
                if type(rule) == str: ranges_per_wflow[rule].append(incl_ranges)
                else:
                    attr, sign, threshold, dest_wflow = rule
                    r_min, r_max = incl_ranges[attr]
                    updated_incl_ranges = dict(incl_ranges)

                    if sign == "<":
                        if r_min < threshold < r_max:
                            updated_incl_ranges.update({attr: (r_min, threshold - 1)})
                            incl_ranges[attr] = (threshold, r_max)

                    elif sign == ">":
                        if r_min < threshold < r_max:
                            updated_incl_ranges.update({attr: (threshold + 1, r_max)})
                            incl_ranges[attr] = (r_min, threshold)

                    ranges_per_wflow[dest_wflow].append(updated_incl_ranges)

total = 0
for r in ranges_per_wflow["A"]:
    combinations = 1
    for v in r.values():
        combinations *= v[1] - v[0] + 1
    total += combinations

print(total)