with open("08/input.txt", "r") as f:
    lines = f.readlines()

move_dict = dict()

instructions = lines[0][:-1]

for line in lines[2:]:
    pos, left, right = line[:3], line[7:10], line[12:15]
    move_dict[pos] = {"L": left, "R": right}

result = 0
found = False
i = 0
instructions_len = len(instructions)
current_pos = "AAA"

while current_pos != "ZZZ":
    instruction = instructions[i]
    
    current_pos = move_dict[current_pos][instruction]

    result += 1
    i = (i + 1) % instructions_len

print(result)
