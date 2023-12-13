def check_map(map_rows):
    for i in range(1, len(map_rows)):
        if check_for_mirror(map_rows, i):
            return i
    return -1

def check_for_mirror(map_rows, possible_mirror):
    return all(a == b for a, b in zip(map_rows[possible_mirror:], map_rows[:possible_mirror][::-1]))


with open("13/input.txt") as f:
    lines = [l[:-1] for l in f.readlines()]

map_buffer = []
maps = []

for i, line in enumerate(lines):
    if line == "":
        maps.append([m for m in map_buffer])
        map_buffer.clear()
    else:
        map_buffer.append(line)
maps.append(map_buffer)

result = 0

for map_rows in maps:
    rows_mirrored = check_map(map_rows)

    if rows_mirrored > 0:
        result += 100 * rows_mirrored
        continue

    map_columns = [''.join(row[i] for row in map_rows) for i in range(len(map_rows[0]))]

    columns_mirrored = check_map(map_columns)
    result += columns_mirrored

print(result)