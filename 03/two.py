def get_neighborhood(y, x_start, x_end, line_length, lines_count):
    neighborhood = set()

    for i in range(y - 1, y + 2):
        for j in range(x_start - 1, x_end + 1):
            if i == y and x_start <= j < x_end:
                continue

            if i >= 0 and j >= 0 and i < lines_count and j < line_length:
                neighborhood.add((i, j))

    return neighborhood


gears = set() # (y, x) == m[y][x]
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
                
                if char == "*":
                    gears.add((i, j))

        if len(number_apps) > 0:
            first_num = number_apps[0]
            last_num = number_apps[-1]

            numbers.add((first_num[0], first_num[1], last_num[1] + 1))


lines_count = len(file_matrix)
result = 0
gears_count = {g: [0, 1] for g in gears}

for y, x_start, x_end in numbers:
    neighbors = get_neighborhood(y, x_start, x_end, line_length, lines_count)
    number = int(file_matrix[y][x_start:x_end])
    
    for g in gears:
        if g in neighbors:
            gears_count[g][0] += 1
            gears_count[g][1] *= number


for g, (count, ratio) in gears_count.items():
    if count > 1:
        result += ratio

print(result)
