import math
max = 99
dial = 50
passw = 0
passw2 = 0
with open("day1example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            dir = -1 if line[0] == 'L' else 1
            move = dir * int(line[1:])
            if dial + move < 0:
                passw2 += math.ceil(((move * -1) - dial) / max)
            elif dial + move > max:
                passw2 += math.ceil((move - dial) / max)
            dial += move
            while dial < 0:
                dial += max + 1
            while dial > max:
                dial -= max + 1
            if dial == 0:
                passw += 1
            print(dial, move, passw, passw2)
print(f'Part 1 Password: {passw}')
print(f'Part 2 Password: {passw2}')
