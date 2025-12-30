import math
import copy

points = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ps = line.split(',')
        points.append(tuple([int(p) for p in ps]))

data = []
for p1 in range(len(points)):
    for p2 in range(p1+1, len(points)):
        data.append([math.dist(points[p1], points[p2]), p1, p2])

memory = sorted(data, key= lambda x: x[0])
print(memory)

connections = 1000
circuits = []

for c in range(connections):
    print(f'Attempt ({connections-c}): ', end='')
    newcp1 = memory[c][1]
    newcp2 = memory[c][2]
    print(points[newcp1], points[newcp2])
    circtoadd = []
    for ix,circuit in enumerate(circuits):
        if points[newcp1] in circuit or points[newcp2] in circuit:
            circtoadd += circuits.pop(ix)
    if points[newcp1] not in circtoadd:
        circtoadd.append(points[newcp1])
    if points[newcp2] not in circtoadd:
        circtoadd.append(points[newcp2])
    circuits.append(circtoadd)

print('------ Circuits: ---------')
for cr in circuits:
    for j in cr:
        print(j[0], end=',')
    print()

sizes = [len(circuit) for circuit in circuits]
sizes = sorted(sizes, reverse=True)
print(sizes)
answer = sizes[0] * sizes[1] * sizes[2]
print('Day 8 Part 1 Answer:', answer)
