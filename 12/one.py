import itertools


with open("12/single.txt", "r") as f:
    lines = [l[:-1] for l in f.readlines()]

result = 0

for line in lines:
    pattern, group_sizes = line.split()
    group_sizes = list(map(int, group_sizes.split(",")))
    operational_group_sizes = [0] + [1 for _ in range(len(group_sizes) - 1)] + [0]

    free_dots = len(pattern) - sum(group_sizes) - sum(operational_group_sizes)
    free_boxes = len(operational_group_sizes)

    required_signs = {i: s for i, s in enumerate(pattern) if s != "?"}

    distributions = set(d for d in itertools.product(range(free_dots + 1), repeat=free_boxes) if sum(d) == free_dots)

    for dist in distributions:
        new_op_groups = [g for g in operational_group_sizes]
        damaged_groups = [g for g in group_sizes]

        for i, added_dots in enumerate(dist):
            new_op_groups[i] += added_dots

        new_pattern = ""

        for i in range(len(new_op_groups) + len(damaged_groups)):
            if i % 2 == 0:
                new_pattern += "." * new_op_groups.pop(0)
            else:
                new_pattern += "#" * damaged_groups.pop(0)

        if all(new_pattern[i] == s for i, s in required_signs.items()):
            result += 1

print(result)
