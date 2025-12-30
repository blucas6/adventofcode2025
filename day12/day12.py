class Shape:
    def __init__(self, id, lines):
        self.id = id
        self.lines = lines
        self.shapes = [self.lines]
        for i in range(3):
            lines = [''.join(list(row)) for row in zip(*lines[::-1])]
            if lines not in self.shapes:
                self.shapes.append(lines)

    def __repr__(self):
        s = f'Shape {self.id}:\n'
        for row in range(len(self.shapes[0])):
            for i,sh in enumerate(self.shapes):
                s += f'{sh[row]} '
            s += '\n'
        return s

sections = []
with open('example.txt', 'r') as f:
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
    grid = grid.split('x')
    pieces = pieces.split()
    problems.append((grid, pieces))

for ix,section in enumerate(sections[:-1]):
    shape = []
    for line in section:
        if ':' not in line:
            shape.append(line.strip())
    shapes.append(Shape(ix, shape))

for shape in shapes:
    print(shape)

print(problem[0])

