with open("18/input.txt") as f:
    plan = [tuple(l.split()) for l in f.read().split("\n")]

i, j = 0, 0
max_i, max_j = 0, 0
min_i, min_j = 0, 0
edges = set()

move = {
    "R": (0, 1),
    "L": (0, -1),
    "D": (1, 0),
    "U": (-1, 0)
}

edges.add((i, j))

for direction, length, color in plan:
    for _ in range(int(length)):
        m_i, m_j = move[direction]
        i, j = i + m_i, j + m_j
        edges.add((i, j))

        if i > max_i: max_i = i
        if j > max_j: max_j = j
        if i < min_i: min_i = i
        if j < min_j: min_j = j

total = 0

for i in range(min_i, max_i):
    edge_count = 0

    for j in range(min_j, max_j):
        if (i, j) in edges:
            edge_up = (i - 1, j) in edges
            edge_down = (i + 1, j) in edges
            edge_left = (i, j - 1) in edges
            edge_right = (i, j + 1) in edges
            edge_desc = list(map(int, [edge_up, edge_right, edge_down, edge_left]))

            if edge_desc == [1, 0, 1, 0]: edge_count += 1
            elif edge_desc in ([1, 1, 0, 0], [0, 1, 1, 0]): edge_start = edge_desc
            elif (edge_desc == [1, 0, 0, 1] and edge_start == [0, 1, 1, 0]) or (edge_desc == [0, 0, 1, 1] and edge_start == [1, 1, 0, 0]): edge_count += 1

        else:
            if edge_count % 2 == 1:
                total += 1

print(total + len(edges))
