def get_neighborhood(y, x_start, x_end, line_length, lines_count):
    neighborhood = []

    for i in range(y - 1, y + 2):
        for j in range(x_start - 1, x_end + 1):
            if i == y and x_start <= j < x_end:
                continue

            if i >= 0 and j >= 0 and i < lines_count and j < line_length:
                neighborhood.append((i, j))

    return neighborhood


symbols = set() # (y, x) == m[y][x]
numbers = set() # (y, x_start, x_end) == m[y][x_start:x_end]
file_matrix = []

with open("input.txt", "r") as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        file_matrix.append(line)
        line_length = len(line)

        number_apps = []

        for j, char in enumerate(line):
            if 47 < ord(char) < 58:
                number_apps.append((i, j))
            else:
                if len(number_apps) > 0:
                    first_num = number_apps[0]
                    last_num = number_apps[-1]

                    numbers.add((first_num[0], first_num[1], last_num[1] + 1))
                    number_apps = []
                
                if char not in (".", "\n"):
                    symbols.add((i, j))

        if len(number_apps) > 0:
            first_num = number_apps[0]
            last_num = number_apps[-1]

            numbers.add((first_num[0], first_num[1], last_num[1] + 1))

lines_count = len(file_matrix)
result = 0

for y, x_start, x_end in numbers:
    neighbors = get_neighborhood(y, x_start, x_end, line_length, lines_count)
    if any(n in symbols for n in neighbors):
        result += int(file_matrix[y][x_start:x_end])

print(result)
