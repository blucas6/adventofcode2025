import math

def whichEdges(points, edges, r, c):
    ix = 0
    mind = math.dist(points[0], (c,r))
    for p,point in enumerate(points):
        dist = math.dist(point, (c,r))
        if dist < mind:
            mind = dist
            ix = p
    nedges = []
    for edge in edges:
        if edge[1] == points[ix] or edge[2] == points[ix]:
            nedges.append(edge)
    return nedges

def isInside(edge, r, c):
    print('Pt:', r, c, ' Closest:', edge)
    dr = edge[0]
    p1 = edge[1]
    p2 = edge[2]
    if dr == 'left':
        print(r, c, p1, p2)
        if r >= p1[1] and r <= p2[1]:
            if c > p1[0]:
                return False
            else:
                return True
    elif dr == 'right':
        if r >= p2[1] and r <= p1[1]:
            if c < p1[0]:
                return False
            else:
                return True
    elif dr == 'below':
        if c >= p1[0] and c <= p2[0]:
            if r < p1[1]:
                return False
            else:
                return True
    elif dr == 'above':
        if c >= p2[0] and c <= p1[0]:
            if r > p1[1]:
                return False
            else:
                return True

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

edges = []
for ix,p in enumerate(points):
    if ix+1 < len(points):
        p2 = points[ix+1]
    else:
        p2 = points[0]
    row = p2[1] - p[1]
    col = p2[0] - p[0]
    if row > 0:
        dr = 'left'
    elif row < 0:
        dr = 'right'
    if col > 0:
        dr = 'below'
    elif col < 0:
        dr = 'above'
    edges.append([dr, p, p2])
print(edges)

pt = (5,10)
print(points)
nedges = whichEdges(points, edges, pt[0], pt[1])
valid = True 
for edge in nedges:
    if not isInside(edge, pt[0], pt[1]):
        valid = False

if valid:
    grid[pt[0]][pt[1]] = 'X'
show(grid)
