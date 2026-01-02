import copy
import time

sleeptime = 0.0

def moverow(row):
    if row < 0:
        print(f'\033[{row*-1}A')
    else:
        print(f'\033[{row}B')

def show(grid, debug='none', redraw=True):
    if debug == 'anim' and redraw:
        time.sleep(sleeptime)
        moverow(-len(grid)-1)
    for row in grid:
        for col in row:
            if col:
                print('#', end='')
            else:
                print('.', end='')
        print()

def findregions(grid):
    seen = [[n for n in row] for row in grid]
    regions = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if not grid[r][c] and not seen[r][c]:
                queue = [(r,c)]
                seen[r][c] = 1
                region = 0
                while queue:
                    cell = queue.pop()
                    region += 1
                    for rx in [-1,0,1]:
                        for cx in [-1,0,1]:
                            row = cell[0]+rx
                            col = cell[1]+cx
                            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                                continue
                            if not grid[row][col] and not seen[row][col]:
                                queue.append((row,col))
                                seen[row][col] = 1

                if region >= 9:
                    regions.append(region)
    return regions

class Shape:
    def __init__(self, id, lines: list[str]):
        self.id = id
        self.lines = lines
        self.shapes = [self.lines]
        for i in range(3):
            lines = [''.join(list(row)) for row in zip(*lines[::-1])]
            if lines not in self.shapes:
                self.shapes.append(lines)
            reflectionh = [row[::-1] for row in lines]
            if reflectionh not in self.shapes:
                self.shapes.append(reflectionh)
            reflectionv = lines[::-1]
            if reflectionv not in self.shapes:
                self.shapes.append(reflectionv)
        
        self.offsets = []
        for r,line in enumerate(self.lines):
            for c,ch in enumerate(line):
                if ch == '#':
                    self.offsets.append((-r,-c))

    def __repr__(self):
        s = f'Shape {self.id}:\n'
        for row in range(len(self.shapes[0])):
            for i,sh in enumerate(self.shapes):
                s += f'{sh[row]} '
            s += '\n'
        return s


def addshape(grid, lines, row, col, debug='none'):
    for r,line in enumerate(lines):
        for c,ch in enumerate(line):
            if ch == '#':
                if (row+r < 0 or row+r >= len(grid) or 
                    col+c < 0 or col+c >= len(grid[0]) or  
                    grid[row+r][col+c] != 0):
                    return False
    for r,line in enumerate(lines):
        for c,ch in enumerate(line):
            if ch == '#':
                grid[row+r][col+c] = 1
    return True

def removeshape(grid, lines, row, col):
    for r,line in enumerate(lines):
        for c,ch in enumerate(line):
            if ch == '#':
                grid[row+r][col+c] = 0


def tryshapenoregions(shapeset, grid, debug='none'):
    if not shapeset:
        return True
    cshape = shapeset[0]
    for rr in range(len(grid)):
        for cc in range(len(grid[0])):
            for shape in cshape.shapes:
                if addshape(grid, shape, rr, cc, debug):
                    if debug != 'none':
                        show(grid, debug)
                    if debug == 'msg':
                        print('added')
                    if tryshapenoregions(shapeset[1:], grid, debug):
                        return True
                    removeshape(grid, shape, rr, cc)
                    if debug == 'msg':
                        print('trying new position')
                    if debug != 'none':
                        show(grid, debug)

    if debug == 'msg':
        print('Failed to add')
    return False

def tryshape(shapeset, grid, debug='none'):
    if not shapeset:
        return True
    cshape = shapeset[0]
    for rr in range(len(grid)):
        for cc in range(len(grid[0])):
            for shape in cshape.shapes:
                if addshape(grid, shape, rr, cc, debug):
                    regions = findregions(grid)
                    needarea = len(shapeset[1:]) * 9
                    if debug != 'none':
                        show(grid, debug)
                    if debug == 'msg':
                        print('Regions:', regions, 'Need:', needarea)
                    if sum(regions) >= needarea:
                        if debug != 'none':
                            show(grid, debug)
                        if debug == 'msg':
                            print('added')
                        if tryshape(shapeset[1:], grid, debug):
                            return True
                    removeshape(grid, shape, rr, cc)
                    if debug == 'msg':
                        print('trying new position')
                    if debug != 'none':
                        show(grid, debug)

    if debug == 'msg':
        print('Failed to add')
    return False

def tryshapeold(shapeset, grid, debug='none'):
    if not shapeset:
        return True
    for rr in range(len(grid)):
        for cc in range(len(grid[0])):
            for cshape in shapeset:
                for shape in cshape.shapes:
                    if addshape(grid, shape, rr, cc, debug):
                        if debug == 'msg':
                            print('added')
                        if debug != 'none':
                            show(grid, debug)
                        if tryshapeold(shapeset[1:], grid, debug):
                            return True
                        removeshape(grid, shape, rr, cc)
                        if debug == 'msg':
                            print('trying new position')
                        if debug != 'none':
                            show(grid, debug)
    if debug == 'msg':
        print('Failed to add')
    return False

def doproblem(problem, shapes, debug='none'):
    print('Problem:', problem)
    grid = [[0 for _ in range(problem[0][0])] for _ in range(problem[0][1])]
    shapestoadd = []
    for ix,shp in enumerate(problem[1]):
        if shp > 0:
            for n in range(shp):
                shapestoadd.append(copy.copy(shapes[ix]))
    minarea = len(shapestoadd) * 7
    if problem[0][0] * problem[0][1] < minarea:
        return False
    time.sleep(sleeptime)
    if debug != 'none':
        show(grid, debug, redraw=False)
    if tryshapenoregions(shapestoadd, grid, debug):
        if debug == 'msg':
            print('Problem:', problem)
        elif debug != 'none':
            show(grid, debug)
        return True
    if debug == 'msg':
        print('Problem:', problem)
    elif debug != 'none':
        show(grid, debug)
    return False

sections = []
debug = 'none'
with open('input.txt', 'r') as f:
    lines = f.readlines()
    section = []
    for line in lines:
        if line != '\n':
            section.append(line)
        else:
            sections.append(section)
            section = []
    sections.append(section)

shapes = []
problems = []
for problem in sections[-1]:
    grid,pieces = problem.split(':')
    grid = [int(n) for n in grid.split('x')]
    pieces = [int(n) for n in pieces.split()]
    problems.append((grid, pieces))

for ix,section in enumerate(sections[:-1]):
    shape = []
    for line in section:
        if ':' not in line:
            shape.append(line.strip())
    shapes.append(Shape(ix, shape))

for shape in shapes:
    print(shape)

solutions = 0
for ix,problem in enumerate(problems):
    print('Working', ix+1, 'out of', len(problems))
    if doproblem(problem, shapes, debug):
        solutions += 1
        print('Solved')
    else:
        print('No solution')
print('Day 12 Part 1 Answer:', solutions)
