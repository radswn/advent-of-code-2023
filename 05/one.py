with open("input.txt", "r") as f:
    lines = f.readlines()

seeds = list(map(int, lines[0][7:].split()))
seeds_number = len(seeds)
changed = [False for _ in range(seeds_number)]

for line in lines[1:]:
    if line == "\n":
        changed = [False for _ in changed]
        continue

    if not 47 < ord(line[0]) < 58:
        continue

    dest_range_start, src_range_start, range_length = list(map(int, line.split()))

    for i in range(seeds_number):
        diff = seeds[i] - src_range_start

        if 0 <= diff < range_length and not changed[i]:
            seeds[i] = dest_range_start + diff
            changed[i] = True

print(min(seeds))
