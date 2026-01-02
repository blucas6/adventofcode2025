max = 99
dial = 50 
passw = 0
passw2 = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            dir = -1 if line[0] == 'L' else 1
            move = int(line[1:])
            simple = int(move / (max+1))
            passw2 += simple
            move -= simple * (max+1) 
            orig = int(dial)
            dial += dir * move
            if dial > max:
                dial -= max + 1
                if orig != 0 and dial != 0:
                    passw2 += 1
            elif dial < 0:
                dial += max + 1
                if orig != 0 and dial != 0:
                    passw2 += 1
            if move != 0 and dial == 0:
                passw += 1
                passw2 += 1
            print(dial, dir*move, simple, passw, passw2)
print(f'Part 1 Password: {passw}')
print(f'Part 2 Password: {passw2}')
