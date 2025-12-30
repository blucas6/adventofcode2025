def trimNodes(nodes, start, end):
    print('Trimming:', start, end)
    currn = None
    queue = [Node(start, nodes[start])]
    allowednodes = []
    while queue:
        currn = queue.pop()
        for output in currn.outputs:
            if output in allowednodes:
                continue
            newnode = Node(output, nodes[output], currn)
            if output == end:
                path = getPath(newnode)
                print('Adding:', path)
                for node in path:
                    if node not in allowednodes:
                        allowednodes.append(node)
                continue
            queue.append(newnode)
    return allowednodes

def getPath(node):
    path = []
    path.append(node.name)
    while node.parent != None:
        node = node.parent
        path.append(node.name)
    return path[::-1]
        
class Node:
    def __init__(self, name, outputs, parent=None):
        self.name = name
        self.outputs = outputs
        self.parent = parent 

    def __repr__(self):
        return f'Name: {self.name} Outputs: {self.outputs} Parent: {self.parent}'

nodes = {}
with open('example2.txt', 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        name = line.split(':')[0]
        outputs = line.split(':')[1].split()
        nodes[name] = outputs
    nodes['out'] = []

allowednodes = trimNodes(nodes, 'dac', 'out')
allowednodes += trimNodes(nodes, 'fft', 'dac')
allowednodes += trimNodes(nodes, 'svr', 'fft')
allowednodes += trimNodes(nodes, 'svr', 'dac')
print(allowednodes)

startnode = 'svr'
endnode = 'out'
queue = [Node(startnode, nodes[startnode])]
currn = None
paths = []
while queue:
    currn = queue.pop()
    print('\tCurrent:', currn)
    for output in currn.outputs:
        newnode = Node(output, nodes[output], currn)
        if output == endnode:
            path = getPath(newnode)
            if 'fft' in path and 'dac' in path:
                print('Adding:', path)
                paths.append(path)
            continue
        if output in allowednodes:
            queue.append(newnode)
print('Result:')
for path in paths:
    print(path)
print('Day 11 Part 2 Answer:', len(paths))
