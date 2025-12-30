import math

points = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        ps = line.split(',')
        points.append(tuple([int(p) for p in ps]))

amountofpoints = len(points)

data = []
for p1 in range(len(points)):
    for p2 in range(p1+1, len(points)):
        data.append([math.dist(points[p1], points[p2]), p1, p2])

memory = sorted(data, key= lambda x: x[0])
circuits = []
success1 = 0
success2 = 0
while memory:
    if circuits and len(circuits[0]) == amountofpoints:
        break
    conn = memory.pop(0)
    print('Memory:', len(memory))
    newcp1 = conn[1]
    newcp2 = conn[2]
    valid = True
    circtoadd = []
    ix = 0
    while ix < len(circuits):
        if points[newcp1] in circuits[ix] and points[newcp2] in circuits[ix]:
            valid = False
            break
        if points[newcp1] in circuits[ix] or points[newcp2] in circuits[ix]:
            circtoadd += circuits.pop(ix)
            ix -= 1
        ix += 1
    if not valid:
        continue
    if points[newcp1] not in circtoadd:
        circtoadd.append(points[newcp1])
    if points[newcp2] not in circtoadd:
        circtoadd.append(points[newcp2])
    circuits.append(circtoadd)
    success1 = points[newcp1]
    success2 = points[newcp2]

print('------ Circuits: ---------')
for cr in circuits:
    for j in cr:
        print(j[0], end=',')
    print()
print()

print('Last connection:', success1, success2)
print('Day 8 Part 2 Answer:', success1[0] * success2[0])
