from itertools import combinations


with open("11/input.txt", "r") as f:
    lines = [l[:-1] for l in f.readlines()]

galaxies = set()
map_size = len(lines), len(lines[0])
occupied_rows = set()
occupied_columns = set()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "#":
            galaxies.add((i, j))
            occupied_rows.add(i)
            occupied_columns.add(j)

empty_rows = set(range(map_size[0])).difference(occupied_rows)
empty_columns = set(range(map_size[1])).difference(occupied_columns)

row_offsets = [sum(row in empty_rows for row in range(i)) for i in range(map_size[0])]
column_offsets = [sum(col in empty_columns for col in range(j)) for j in range(map_size[1])]

expanded_galaxies = [(i + row_offsets[i], j + column_offsets[j]) for i, j in galaxies]

galaxy_pairs = combinations(range(len(expanded_galaxies)), 2)

total_distance = 0

for a, b in galaxy_pairs:
    a_i, a_j = expanded_galaxies[a]
    b_i, b_j = expanded_galaxies[b]

    diff_i = abs(a_i - b_i)
    diff_j = abs(a_j - b_j)

    total_distance += diff_i + diff_j

print(total_distance)
