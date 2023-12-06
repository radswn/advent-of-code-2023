import math

with open("06/input.txt", "r") as f:
    race_time = int("".join(f.readline()[6:].split()))
    race_record = int("".join(f.readline()[9:].split()))

delta_sqrt = (race_time**2 - 4 * race_record) ** 0.5

limit_1 = (-race_time - delta_sqrt)/-2
limit_2 = (-race_time + delta_sqrt)/-2

lower_limit, upper_limit = sorted([limit_1, limit_2])

result = math.floor(upper_limit - 0.00000000001) - math.ceil(lower_limit + 0.00000000001) + 1

print(result)
