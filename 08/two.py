import math

with open("08/input.txt", "r") as f:
    lines = f.readlines()

move_dict = dict()

instructions = lines[0][:-1]
starting_positions = set()

for line in lines[2:]:
    pos, left, right = line[:3], line[7:10], line[12:15]
    move_dict[pos] = {"L": left, "R": right}
    
    if pos.endswith("A"):
        starting_positions.add(pos)

steps_needed = set()
instructions_len = len(instructions)

for start in starting_positions:
    result = 0
    i = 0
    current_pos = start

    while not current_pos.endswith("Z"):
        instruction = instructions[i]
        
        current_pos = move_dict[current_pos][instruction]

        result += 1
        i = (i + 1) % instructions_len

    steps_needed.add(result)

result = math.lcm(*steps_needed)
print(result)
