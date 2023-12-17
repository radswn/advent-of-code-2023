import math
from queue import PriorityQueue


def get_neighbors(position, direction, continous_counter, max_i, max_j):
    neighbors = set()
    i, j = position

    if (direction != "n") and not (direction == "s" and continous_counter == 3) and (i < max_i - 1):
        neighbors.add((i + 1, j, "s"))

    if (direction != "e") and not (direction == "w" and continous_counter == 3) and (j > 0):
        neighbors.add((i, j - 1, "w"))

    if (direction != "s") and not (direction == "n" and continous_counter == 3) and (i > 0):
        neighbors.add((i - 1, j, "n"))

    if (direction != "w") and not (direction == "e" and continous_counter == 3) and (j < max_j - 1):
        neighbors.add((i, j + 1, "e"))

    return neighbors


with open("17/input.txt", "r") as f:
    mmap = [[int(n) for n in l] for l in f.read().split("\n")]

rows, cols = len(mmap), len(mmap[0])

start = (0, 0, "e", 1)
finish = (rows - 1, cols - 1)

dist = {(i, j, d, c): math.inf for i in range(rows) for j in range(cols) for d in ("n", "e", "s", "w") for c in range(1, 4)}
unvisited = PriorityQueue()
previous = {(i, j): None for i in range(rows) for j in range(cols)}

dist[start] = 0
unvisited.put((0, (0, 0), "e", 1))
previous[start] = None

while not unvisited.empty():
    current_dist, current, current_direction, current_counter = unvisited.get()

    neighbors = get_neighbors(current, current_direction, current_counter, rows, cols)

    for n_i, n_j, n_direction in neighbors:
        alt = current_dist + mmap[n_i][n_j]

        if n_direction == current_direction:
            n_counter = current_counter + 1
        else:
            n_counter = 1

        n = (n_i, n_j, n_direction, n_counter)

        if alt < dist[n]:
            dist[n] = alt
            unvisited.put((alt, (n_i, n_j), n_direction, n_counter))
            previous[n] = current


result = min(dist[(rows - 1, cols - 1, d, c)] for d in ("n", "e", "s", "w") for c in range(1, 4))

print(result)
