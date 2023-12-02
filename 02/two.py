with open("input.txt", "r") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        split_line = line.split(":")
        game_id = int(split_line[0].split()[1])

        observations = split_line[1].strip().split(";")

        possible = True

        fewest = {k: 0 for k in ("red", "green", "blue")}

        for obs in observations:
            ball_counts = obs.split(",")

            for bc in ball_counts:
                count, color = bc.strip().split()
                fewest[color] = max(fewest[color], int(count))

        power = fewest["red"] * fewest["green"] * fewest["blue"]
        result += power


print(result)