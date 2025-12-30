import time
import os

os.system("")

def moverow(row):
    if row < 0:
        print(f'\033[{row*-1}A')
    else:
        print(f'\033[{row}B')

def show(board):
    for r in board:
        print(r)

answer = 0
board = []
with open('example.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        board.append(line.strip())

start = board[0].find('S')
row = 1
board[row] = board[row][:start] + '|' + board[row][start+1:]
show(board)
sleeptime = 0.5

while row < len(board)-1:
    time.sleep(sleeptime)
    for ix,ch in enumerate(board[row]):
        if ch == '|':
            if board[row+1][ix] == '^':
                board[row+1] = board[row+1][:ix-1] + '|' + board[row+1][ix] + '|' + board[row+1][ix+2:]
                answer += 1
            else:
                board[row+1] = board[row+1][:ix] + '|' + board[row+1][ix+1:]
    moverow(-len(board)-1)
    show(board)
    row += 1

print()
print('Day 7 Part 1 Answer:', answer)



