with open("14/input.txt", "r") as f:
    rocks = [l[:-1] for l in f.readlines()]

rock_columns = [''.join(row[i] for row in rocks) for i in range(len(rocks[0]))]

max_load = len(rocks)
total_load = 0

for column in rock_columns:
    position_load = max_load
    column_load = 0

    for i, rock in enumerate(column):
        if rock == "O":
            column_load += position_load
            position_load -= 1
        elif rock == "#":
            position_load = max_load - i - 1
    
    total_load += column_load

print(total_load)
