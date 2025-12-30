import math

def show(grid):
    for row in grid:
        for col in row:
            print(col, end='')
        print()

display = True
points = []

with open('example.txt', 'r') as f:
    lines = f.readlines()
    points = [tuple([int(line.split(',')[0]),int(line.split(',')[1])]) for line in lines]

if display:
    maxcols = max(x for x,y in points) + 2
    maxrows = max(y for x,y in points) + 2
    grid = [['.' for c in range(maxcols)] for r in range(maxrows)]
    for point in points:
        grid[point[1]][point[0]] = '#'
    show(grid)

data = []
for p1 in range(len(points)):
    for p2 in range(p1+1, len(points)):
        sz = (1+abs(points[p1][0]-points[p2][0])) * (1+abs(points[p1][1]-points[p2][1]))
        data.append([sz, points[p1], points[p2]])

data = sorted(data, key=lambda x: x[0])
p1 = data[-1][1]
p2 = data[-1][2]
print('Biggest:', p1, p2)
l = abs(p1[0]-p2[0]) + 1
w = abs(p1[1]-p2[1]) + 1
print('Area:', l, '*', w, '=', l*w)

if display:
    bigrow = max(p1[1], p2[1])
    bigcol = max(p1[0], p2[0])
    smrow = min(p1[1], p2[1])
    smcol = min(p1[0], p2[0])
    for r,row in enumerate(grid):
        for c,col in enumerate(row):
            if (r == p1[1] and c == p1[0]) or (r == p2[1] and c == p2[0]):
                continue
            if r <= bigrow and r >= smrow and c <= bigcol and c >= smcol:
                grid[r][c] = 'O'
    show(grid)
