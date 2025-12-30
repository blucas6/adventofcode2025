lines = []
with open('input.txt', 'r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]

ranges = []
ids = {}
for line in lines:
    if '-' in line:
        start = int(line.split('-')[0])
        end = int(line.split('-')[1])
        ranges.append([start, end])
    else:
        ids[int(line)] = False
print('Ranges', ranges)

for id in ids.keys():
    for rang in ranges:
        if rang[0] < id and rang[1]+1 > id:
            ids[id] = True

fresh = 0
for id in ids.keys():
    print(id, ids[id])
    if ids[id]:
        fresh += 1
print('Day 5 Part 1 Answer:', fresh)

fresh = 0
newranges = []
for expand in ranges:
    start = expand[0]
    end = expand[1]
    for nr in newranges:
        if start > nr[0] and start < nr[1]:
            start = nr[1]+1
        elif end > nr[0] and end < nr[1]:
            end = nr[0]-1
    if not start > end:
        newranges.append([start, end])

for nr in newranges:
    print(nr)
    fresh += nr[1] - nr[0] + 1

print('Day 5 Part 2 Answer:', fresh)

