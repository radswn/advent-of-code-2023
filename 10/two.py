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


def find_replacement(position, grid):
    i, j = position
    up = grid[i - 1][j] in ("|", "F", "7")
    down = grid[i + 1][j] in ("|", "L", "J")
    left = grid[i][j - 1] in ("-", "F", "L")
    right = grid[i][j + 1] in ("-", "J", "7")

    if up and down:
        return "|"
    if up and right:
        return "L"
    if up and left:
        return "J"
    if down and left:
        return "7"
    if down and right:
        return "F"
    return "-"


with open("10/input.txt", "r") as f:
    grid = f.readlines()

grid_limits = len(grid), len(grid[0])
neighborhood_queue = Queue()
visited = set()
start = None
result = 0

for i, line in enumerate(grid):
    for j, char in enumerate(line):
        if char == "S":
            start = (i, j)

all_positions = set({(i, j) for i in range(grid_limits[0]) for j in range(grid_limits[1])})
neighborhood_queue.put((start, 0))

while not neighborhood_queue.empty():
    position, distance = neighborhood_queue.get()

    if position in visited:
        continue

    visited.add(position)
    neighbors = get_neighbors(position, grid)

    for n in neighbors:
        neighborhood_queue.put((n, distance + 1))

non_loop_positions = all_positions.difference(visited)

start_replacement = find_replacement(start, grid)
start_row = grid[start[0]]
start_row = list(start_row)
start_row[start[1]] = start_replacement
grid[start[0]] = "".join(start_row)

for i in range(grid_limits[0]):
    edge_count = 0
    for j in range(grid_limits[1]):
        if (i, j) in non_loop_positions:
            if edge_count % 2 == 1:
                result += 1
        else:
            if grid[i][j] == "|":
                edge_count += 1
            elif grid[i][j] in ("L", "F"):
                edge_start = grid[i][j]
            elif (grid[i][j] == "J" and edge_start == "F") or (grid[i][j] == "7" and edge_start == "L"):
                edge_count += 1

print(result)
