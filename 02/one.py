limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

limits_leftovers = {
    k: sum(limits.values())-limits[k] for k in limits
}

with open("input.txt", "r") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        split_line = line.split(":")
        game_id = int(split_line[0].split()[1])

        observations = split_line[1].strip().split(";")

        possible = True

        for obs in observations:
            ball_counts = obs.split(",")
            total = {}

            for bc in ball_counts:
                count, color = bc.strip().split()
                total[color] = int(count)

            if any(v > limits_leftovers[k] or v > limits[k] for k, v in total.items()):
                possible = False

        if possible:
            result += game_id

print(result)