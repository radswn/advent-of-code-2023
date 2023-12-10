from queue import Queue


def get_neighbors(position, grid):
    i, j = position

    pipe = grid[i][j]

    if pipe == "|":
        neighbors = [(i - 1, j), (i + 1, j)]
    elif pipe == "-":
        neighbors = [(i, j - 1), (i, j + 1)]
    elif pipe == "L":
        neighbors = [(i - 1, j), (i, j + 1)]
    elif pipe == "J":
        neighbors = [(i - 1, j), (i, j - 1)]
    elif pipe == "7":
        neighbors = [(i + 1, j), (i, j - 1)]
    elif pipe == "F":
        neighbors = [(i + 1, j), (i, j + 1)]
    elif pipe == "S":
        neighbors = []
        for n_i, n_j in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
            if n_i == i - 1 and n_j == j and grid[n_i][n_j] in ("|", "F", "7"):
                neighbors.append((n_i, n_j))
            elif n_i == i + 1 and n_j == j and grid[n_i][n_j] in ("|", "L", "J"):
                neighbors.append((n_i, n_j))
            elif n_i == i and n_j == j - 1 and grid[n_i][n_j] in ("-", "F", "L"):
                neighbors.append((n_i, n_j))
            elif n_i == i and n_j == j + 1 and grid[n_i][n_j] in ("-", "J", "7"):
                neighbors.append((n_i, n_j))
    
    return neighbors


with open("10/input.txt", "r") as f:
    grid = f.readlines()

grid_limit = len(grid)

start = None

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)

neighborhood_queue = Queue()
visited = set()

neighborhood_queue.put((start, 0))

while not neighborhood_queue.empty():
    position, distance = neighborhood_queue.get()

    if position in visited:
        continue

    visited.add(position)

    neighbors = get_neighbors(position, grid)

    for n in neighbors:
        neighborhood_queue.put((n, distance + 1))

print(distance - 1)