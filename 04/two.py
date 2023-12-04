from queue import Queue

processed = 0
to_process = Queue()
hits_db = []

with open("input.txt", "r") as f:
    lines = f.readlines()


for i, line in enumerate(lines):
    winning_numbers, your_numbers = map(str.strip, line.split(":")[1].split("|"))
    winning_numbers, your_numbers = set(map(int, winning_numbers.split())), set(map(int, your_numbers.split()))

    hits = len(your_numbers.intersection(winning_numbers))
    hits_db.append(hits)
    to_process.put(i)


while not to_process.empty():
    id_to_process = to_process.get()
    processed += 1
    
    hits_for_id = hits_db[id_to_process]

    for h in range(id_to_process + 1, id_to_process + 1 + hits_for_id):
        to_process.put(h)
    
print(processed)