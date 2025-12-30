import time

def movexy(x,y):
    if x < 0:
        print(f'\033[{x*-1}A')
    if x > 0:
        print(f'\033[{x}B')
    if y < 0:
        print(f'\033[{y*-1}C')
    if y > 0:
        print(f'\033[{y}D')

def showgrid(lines):
    movexy(-1*len(lines)-1, 0)
    for line in lines:
        print(line)

total = 0
lines = []
with open('input.txt', 'r') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines if line.strip()]
rows = len(lines)
cols = len(lines[0])
print('Rows:', rows, 'Cols:', cols)
for r in range(rows):
    if r == 0:
        print('<', end='')
    elif r == rows-1:
        print('>')
    else:
        print('-', end='')
for c in range(cols-1):
    if c == cols-2:
        print('v')
    else:
        print('|')
input('Please extend your terminal <enter>')
movexy(-2, 0)
print('\033[2K', end='\r')
movexy(-1, 0)
done = False 
with open('output.txt', 'w+') as ofile:
    while not done:
        done = True
        time.sleep(0.5)
        showgrid(lines)
        for rw, line in enumerate(lines):
            if not line:
                continue
            for cl,chr in enumerate(line):
                rolls = 0
                if chr == '@':
                    for r in range(-1, 2):
                        for c in range(-1, 2):
                            if (rw+r < 0 or rw+r >= rows or cl+c < 0 or cl+c >= cols or
                                (r == 0 and c == 0)):
                                continue
                            if lines[rw+r][cl+c] == '@':
                                rolls += 1
                    if rolls < 4:
                        done = False
                        total += 1
                        ofile.write('x')
                        segment = list(lines[rw])
                        segment[cl] = '.'
                        lines[rw] = ''.join(segment)
                    else:
                        ofile.write('@')
                else:
                    ofile.write('.')
            ofile.write('\n')
        ofile.write('\n')
print(f'Answer Part 2: {total}')
