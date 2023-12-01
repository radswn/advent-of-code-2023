def is_number(char):
    return char in {f"{x}" for x in range(10)}


with open("input.txt", "r") as f:
    lines = f.readlines()

    result = 0

    for line in lines:
        stripped = list(filter(is_number, line))

        if len(stripped) == 1:
            number = stripped[0]
            result += int(number + number)
        else:
            result += int(stripped[0] + stripped[-1])

print(result)
