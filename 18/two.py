def hex_to_instruction(hex):
    distance, direction = hex[0:5], hex[5]
    return ["R", "D", "L", "U"][int(direction)], int(distance, 16)


def get_move(x, y, direction, distance):
    if direction == "R":
        return x + distance, y
    elif direction == "D":
        return x, y - distance
    elif direction == "L":
        return x - distance, y
    else:
        return x, y + distance


with open("18/input.txt") as f:
    plan = [hex_to_instruction(l.split()[-1][2:-1]) for l in f.read().split("\n")]

x, y = 0, 0
total = 0

for direction, distance in plan:
    next_x, next_y  = get_move(x, y, direction, distance)

    p = -0.5 * (x * next_y - y * next_x)
    total += p

    x, y = next_x, next_y
    total += distance / 2

print(int(total) + 1)
