def hash(string):
    current_value = 0
    
    for char in string:
        current_value += ord(char)
        current_value = (17 * current_value) % 256
    
    return current_value
        

with open("15/input.txt", "r") as f:
    sequence = f.read().split(",")

result = 0

for step in sequence:
    result += hash(step)

print(result)
