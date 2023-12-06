import math

with open("06/input.txt", "r") as f:
    times = list(map(int, f.readline()[6:].split()))
    records = list(map(int, f.readline()[9:].split()))

result = 1

for race_time, race_record in zip(times, records):
    delta_sqrt = (race_time**2 - 4 * race_record) ** 0.5

    limit_1 = (-race_time - delta_sqrt)/-2
    limit_2 = (-race_time + delta_sqrt)/-2

    lower_limit, upper_limit = sorted([limit_1, limit_2])

    ways_to_beat = math.floor(upper_limit - 0.00000000001) - math.ceil(lower_limit + 0.00000000001) + 1

    if ways_to_beat > 0:
        result *= ways_to_beat

print(result)
