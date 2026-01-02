def show(grid):
    for row in grid:
        print(row)

grid = ['#######..#..#..#..#..#..#######.####..',
    '#..#..#######################......###',
    '######...................######.......']

show(grid)

seen = []
regions = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '.' and (r,c) not in seen:
            queue = [(r,c)]
            seen.append((r,c))
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
                        if grid[row][col] == '.' and (row,col) not in seen:
                            queue.append((row,col))
                            seen.append((row,col))

            regions.append(region)
print(regions)

