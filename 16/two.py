from queue import Queue


with open("16/input.txt", "r") as f:
    tiles = f.read().split("\n")


limit_x, limit_y = len(tiles[0]) - 1, len(tiles) - 1
possible_starts = set()

for i in range(limit_y):
    possible_starts.add(((i, 0), "e"))
    possible_starts.add(((i, limit_x), "w"))

for j in range(limit_x):
    possible_starts.add(((0, j), "s"))
    possible_starts.add(((limit_y, j), "n"))

most_energized = 0

for start, direction in possible_starts:
    energized = set()
    memory = set()
    to_visit = Queue()
    to_visit.put((start, direction))

    while not to_visit.empty():
        current, current_direction = to_visit.get()

        if not (0 <= current[0] <= limit_y and 0 <= current[1] <= limit_x) or ((current, current_direction) in memory):
            continue

        i, j = current
        tile = tiles[i][j]

        if (current_direction == "n" and tile in ("|", ".")) or (current_direction == "w" and tile in ("\\", "|")) or (current_direction == "e" and tile in ("/", "|")):
            to_visit.put(((i - 1, j), "n"))
        
        if (current_direction == "n" and tile in ("/", "-")) or (current_direction == "s" and tile in ("\\", "-")) or (current_direction == "e" and tile in ("-", ".")):
            to_visit.put(((i, j + 1), "e"))
        
        if (current_direction == "n" and tile in ("\\", "-")) or (current_direction == "s" and tile in ("/", "-")) or (current_direction == "w" and tile in ("-", ".")):
            to_visit.put(((i, j - 1), "w"))
        
        if (current_direction == "s" and tile in ("|", ".")) or (current_direction == "w" and tile in ("/", "|")) or (current_direction == "e" and tile in ("\\", "|")):
            to_visit.put(((i + 1, j), "s"))

        energized.add(current)
        memory.add((current, current_direction))

    most_energized = max(most_energized, len(energized))

print(most_energized)