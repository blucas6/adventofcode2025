class Node:
    def __init__(self, value, button):
        self.value = value
        self.button = button
        self.trace = []

    def __repr__(self):
        return f'Node: {self.value} Button: {self.button} trace: {self.trace}'

def pressBattery(battery, button):
    newbattery = list(battery)
    for press in button:
        if press in newbattery:
            newbattery.pop(newbattery.index(press))
        else:
            newbattery.append(press)
    return newbattery

def solve(machine):
    print('Solving:', machine)
    battery = machine[0]
    buttons = machine[1]
    queue = [Node(battery, None)]
    found = False
    currn = None
    while queue:
        currn = queue.pop(0)
        #print('Visiting:', currn)
        for button in buttons:
            if button in currn.trace:
                continue
            newb = pressBattery(currn.value, button)
            node = Node(newb, button)
            node.trace += currn.trace + [button]
            #print('\tAdding:', node)
            queue.append(node)
            if not newb:
                currn = node
                found = True
                break
        if found:
            break
    return currn.trace

machines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l,line in enumerate(lines):
        sections = line.split()
        battery = []
        for c,ch in enumerate(sections[0]):
            if ch == '#':
                battery.append(c-1)
        buttons = []
        for button in sections[1:-1]:
            button = button[1:-1].split(',')
            button = [int(b) for b in button]
            buttons.append(list(button))
        machines.append([battery, buttons])

answer = 0
for machine in machines:
    answer += len(solve(machine))

print('Day 10 Part 1 Answer:', answer)
