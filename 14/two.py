def move_cycle(moves, round_rocks):
    round_rocks = move_rocks(moves["n"], round_rocks, "n")
    round_rocks = move_rocks(moves["w"], round_rocks, "w")
    round_rocks = move_rocks(moves["s"], round_rocks, "s")
    round_rocks = move_rocks(moves["e"], round_rocks, "e")

    return round_rocks


def move_rocks(moves, round_rocks, direction):
    moved_rocks = set()

    for r_rock in round_rocks:
        move_destination = moves[r_rock]

        while move_destination in moved_rocks:
            move_destination = adjust_move(move_destination, direction)

        moved_rocks.add(move_destination)

    return moved_rocks


def adjust_move(move, direction):
    i, j = move
    if direction == "n":
        return (i + 1, j)
    elif direction == "w":
        return (i, j + 1)
    elif direction == "s":
        return (i - 1, j)
    else:
        return (i, j - 1)


def calculate_load(rocks, max_load):
    total_load = 0
    for i, _ in rocks:
        total_load += max_load - i

    return total_load


with open("14/input.txt", "r") as f:
    rocks = [l[:-1] for l in f.readlines()]

round_rocks = set()
square_rocks = set()
height = len(rocks)
length = len(rocks[0])

move_map = dict({
    d: dict({(i, j): (i, j) for i in range(len(rocks)) for j in range(len(rocks))})
    for d in ("n", "w", "s", "e")
})

for i, row in enumerate(rocks):
    place_to_move = (i, 0)

    for j, rock in enumerate(row):
        if rock == "#":
            place_to_move = (i, j+1)
            continue

        if rock == "O":
            round_rocks.add((i, j))

        move_map["w"][(i, j)] = place_to_move

    place_to_move = (i, length - 1)

    for j, rock in enumerate(row[::-1]):
        j = length - j - 1
        if rock == "#":
            place_to_move = (i, j-1)
            continue

        move_map["e"][(i, j)] = place_to_move

rock_columns = [''.join(row[i] for row in rocks) for i in range(len(rocks[0]))]
for j, row in enumerate(rock_columns):
    place_to_move = (0, j)

    for i, rock in enumerate(row):
        if rock == "#":
            place_to_move = (i + 1, j)
            continue

        move_map["n"][(i, j)] = place_to_move

    place_to_move = (height - 1, j)

    for i, rock in enumerate(row[::-1]):
        i = height - i - 1
        if rock == "#":
            place_to_move = (i - 1, j)
            continue

        move_map["s"][(i, j)] = place_to_move

visited = dict()
i = 1
cycle_end = 0
cycle_start = 0

while True:
    round_rocks = move_cycle(move_map, round_rocks)

    if round_rocks in visited.values():
        cycle_end = i
        cycle_start = [k for k in visited if visited[k] == round_rocks][0]
        break

    visited[i] = round_rocks
    i += 1

cycle_length = cycle_end - cycle_start
position_to_check = cycle_start  + (1000000000 - cycle_start) % cycle_length

print(calculate_load(visited[position_to_check], len(rocks)))
