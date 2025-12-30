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
        newbattery[press] -= 1
    return newbattery

def solve(machine):
    print('Solving:', machine)
    battery = machine[0]
    buttons = machine[1]
    queue = [Node(battery, None)]
    found = False
    currn = None
    level = 0
    while queue:
        currn = queue.pop(0)
        if len(currn.trace) > level:
            print('Level', level)
            level = len(currn.trace)
        #print('Visiting:', currn)
        for button in buttons:
            newb = pressBattery(currn.value, button)
            if min(newb) < 0:
                continue
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
with open('example.txt', 'r') as f:
    lines = f.readlines()
    for l,line in enumerate(lines):
        sections = line.split()
        voltage = sections[-1][1:-1].split(',')
        battery = [int(v) for v in voltage]
        buttons = []
        for button in sections[1:-1]:
            button = button[1:-1].split(',')
            button = [int(b) for b in button]
            buttons.append(list(button))
        machines.append([battery, buttons])
answer = 0
'''
for machine in machines:
    answer += len(solve(machine))
    '''
solve(machines[0])

print('Day 10 Part 1 Answer:', answer)
