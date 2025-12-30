total = 0
with open('output.txt', 'w+') as ofile:
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        rows = len(lines)
        cols = len(lines[0])
        print('Rows:', rows, 'Cols:', cols)
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
                        total += 1
                        ofile.write('x')
                    else:
                        ofile.write('@')
                else:
                    ofile.write('.')
            ofile.write('\n')
print(f'Answer Part 1: {total}')
