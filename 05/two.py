with open("input.txt", "r") as f:
    lines = f.readlines()

seeds = list(map(int, lines[0][7:].split()))
seed_ranges = []

for i in range(0, len(seeds), 2):
    seed_ranges.append((seeds[i], seeds[i] + seeds[i+1]))

modifications = []
buffer = []

for line in lines[1:]:
    if line == "\n":
        if len(buffer):
            modifications.append(buffer)
        buffer = []
        continue

    if not 47 < ord(line[0]) < 58:
        continue

    dest_range_start, src_range_start, range_length = list(map(int, line.split()))
    
    src_range_end = src_range_start + range_length
    dest_range_end = dest_range_start + range_length
    difference = src_range_start - dest_range_start
    
    buffer.append((dest_range_start, dest_range_end, difference))


modifications.append(buffer)

modifications = modifications[::-1]

location_guess = 0
found = False
while not found:
    seed_guess = location_guess

    for mod in modifications:
        for range_start, range_end, diff in mod:
            if range_start <= seed_guess < range_end:
                seed_guess += diff
                break

    for s_range in seed_ranges:
        start, end = s_range

        if start <= seed_guess < end:
            found = True
            print(location_guess)
            break
    
    location_guess += 1
