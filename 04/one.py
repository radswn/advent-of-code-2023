result = 0

with open("input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        winning_numbers, your_numbers = map(str.strip, line.split(":")[1].split("|"))
        winning_numbers, your_numbers = set(map(int, winning_numbers.split())), set(map(int, your_numbers.split()))

        hits = len(your_numbers.intersection(winning_numbers))

        if hits > 0:
            result += 2 ** (hits - 1)

print(result)
