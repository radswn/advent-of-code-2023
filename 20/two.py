from collections import defaultdict
from queue import Queue
from math import prod


with open("20/input.txt") as f:
    modules = f.read().split("\n")

m_types = dict()
m_destinations = dict()
m_inputs = defaultdict(list)
m_memory = dict()

for m in modules:
    inp, dest = m.replace(" ", "").split("->")
    m_type, inp = inp[0], inp[1:]
    dests = dest.split(",")
    if m_type == "b": inp = m_type + inp
    m_types[inp] = m_type
    m_destinations[inp] = dests
    for d in dests: m_inputs[d].append(inp)

for m, inputs in m_inputs.items():
    if m not in m_types: continue

    if m_types[m] == "%": m_memory[m] = False
    elif m_types[m] == "&": m_memory[m] = {i: False for i in inputs}

button_pushes = 0
fewest_for_rx = dict()

while True:
    signal_queue = Queue()
    signal_queue.put(("button", "broadcaster", False))
    button_pushes += 1

    while not signal_queue.empty():
        from_module, to_module, signal = signal_queue.get()
        
        if to_module in ("sp", "pg", "sv", "qs") and not signal and to_module not in fewest_for_rx: fewest_for_rx[to_module] = button_pushes

        if to_module not in m_types: continue

        if m_types[to_module] == "%":
            if not signal:
                m_memory[to_module] = not m_memory[to_module]
                output = m_memory[to_module]
            else: continue

        elif m_types[to_module] == "&":
            m_memory[to_module][from_module] = signal
            output = not all(p for p in m_memory[to_module].values())

        else: output = signal

        for d in m_destinations[to_module]: signal_queue.put((to_module, d, output))

    if len(fewest_for_rx) == 4: break

print(prod(fewest_for_rx.values()))
