
answer = 0
board = []
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        board.append(line.strip())

start = board[0].find('S')
beams = [[0 for c in range(len(board[0]))] for r in range(len(board))]
beams[1][start] = 1

for row in range(1, len(board)-1):
    print('\rRow:', row, 'out of', len(board)-2, end='')
    for col in range(len(board[0])):
        if beams[row][col] > 0:
            if board[row+1][col] == '^':
                beams[row+1][col-1] += beams[row][col]
                beams[row+1][col+1] += beams[row][col]
            else:
                beams[row+1][col] += beams[row][col]
print()
print(beams[-1])
print(sum(beams[-1]))
