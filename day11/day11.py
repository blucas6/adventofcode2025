class Node:
    def __init__(self, name, outputs):
        self.name = name
        self.outputs = outputs

    def __repr__(self):
        return f'Name: {self.name} Outputs: {self.outputs}'

nodes = {}
with open('input.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        name = line.split(':')[0]
        outputs = line.split(':')[1].split()
        nodes[name] = Node(name, outputs)

print(nodes)

queue = [nodes['you']]
currn = None
paths = 0
while queue:
    currn = queue.pop()
    print('\tCurrent:', currn)
    for output in currn.outputs:
        if output == 'out':
            paths += 1
            continue
        queue.append(nodes[output])
print('Day 11 Part 1 Answer:', paths)

    

