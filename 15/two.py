def hash(string):
    current_value = 0
    
    for char in string:
        current_value += ord(char)
        current_value = (17 * current_value) % 256
    
    return current_value
        

with open("15/input.txt", "r") as f:
    sequence = f.read().split(",")

result = 0
boxes = dict({i: [] for i in range(256)})
label_to_focal = dict()

for step in sequence:
    if step[-1] != "-":
        label, operation, focal_length = step[:-2], step[-2], int(step[-1])
    else:
        label, operation = step[:-1], step[-1]

    box_id = hash(label)

    if operation == "-" and label in boxes[box_id]:
        boxes[box_id].remove(label)
    elif operation == "=":
        label_to_focal[label] = focal_length
        if label not in boxes[box_id]:
            boxes[box_id].append(label)

result = 0
for box_id, box in boxes.items():
    for i, label in enumerate(box):
        result += (box_id + 1) * (i + 1) * label_to_focal[label]

print(result)
