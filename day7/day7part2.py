import time
import os
import copy

os.system("")

def moverow(row):
    if row < 0:
        print(f'\033[{row*-1}A')
    else:
        print(f'\033[{row}B')

def show(board, beams):
    display = [r for r in board]
    for beam in beams:
        display[beam[0]] = display[beam[0]][:beam[1]] + '|' + display[beam[0]][beam[1]+1:]
    for row in display:
        print(row)

answer = 0
board = []
with open('example.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        board.append(line.strip())

display = True
start = board[0].find('S')
row = 1
beams = []
beams.append([row, start])
sleeptime = 0.1
queue = [[beams, row]]

while queue:
    beams, row = queue.pop()
    answer += 1
    if display:
        print('Beam:', answer)
        show(board, beams)
        time.sleep(sleeptime)
    else:
        print('Beam:', answer, end='\r')
    while row < len(board)-1:
        for ix,ch in enumerate(board[row]):
            if [row, ix] in beams:
                if board[row+1][ix] == '^':
                    # right
                    newbeams = beams + [[row+1, ix+1]]
                    queue.append([newbeams, row+1])
                    # left
                    beams.append([row+1,ix-1])
                else:
                    beams.append([row+1, ix])
        if display:
            moverow(-len(board)-1)
            show(board, beams)
            time.sleep(sleeptime)
        row += 1
    if display:
        moverow(-len(board)-2)

moverow(len(board)+1)
print('Day 7 Part 2 Answer:', answer)
