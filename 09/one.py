def extrapolate(numbers):
    if not any(numbers):
        return 0

    return numbers[-1] + extrapolate([numbers[i] - numbers[i - 1] for i in range(1, len(numbers))])


with open("09/input.txt", "r") as f:
    lines = f.readlines()

result = 0

for line in lines:
    numbers = list(map(int, line.split()))

    result += extrapolate(numbers)

print(result)