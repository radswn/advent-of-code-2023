import functools


@functools.cache
def count_arrangements(pattern, arrangements, ongoing=0):
    if len(pattern) == 0:
        if (len(arrangements) == 0 and ongoing == 0) or (len(arrangements) == 1 and ongoing == arrangements[0]):
            return 1
        else:
            return 0

    if len(arrangements) == 0 and ongoing > 0:
        return 0

    if pattern[0] == ".":
        if len(arrangements) > 0:
            if arrangements[0] == ongoing:
                arrangements = arrangements[1:]
            elif ongoing > 0:
                return 0
        return count_arrangements(pattern[1:], arrangements)
    elif pattern[0] == "?":
        if len(arrangements) == 0:
            return count_arrangements("." + pattern[1:], arrangements, ongoing)

        return count_arrangements("." + pattern[1:], arrangements, ongoing) + count_arrangements("#" + pattern[1:], arrangements, ongoing)
    else:
        return count_arrangements(pattern[1:], arrangements, ongoing + 1)


with open("12/input.txt", "r") as f:
    lines = [l[:-1] for l in f.readlines()]

result = 0

for c, line in enumerate(lines):
    pattern, groups_required = line.split()
    pattern = "?".join(pattern for _ in range(5))
    groups_required = tuple(map(int, groups_required.split(","))) * 5

    line_result = count_arrangements(pattern, groups_required)

    result += line_result

print(result)
