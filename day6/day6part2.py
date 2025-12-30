import copy

answer = 0
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

index = [-1]
for c,ch in enumerate(lines[0]):
    if ch == ' ':
        if all(True if lines[x][c]==' ' else False for x in range(len(lines))):
            index.append(c)
index.append(len(lines[0])-1)

for ind in range(1, len(index)):
    end = index[ind-1]
    st = index[ind]-1
    prob = []
    for cl in range(st, end, -1):
        nm = ''
        for r in range(len(lines)-1):
            try:
                if lines[r][cl] != ' ' and lines[r][cl] != '\n':
                    nm += lines[r][cl]
            except:
                break
        prob.append(int(nm))
    ans = copy.copy(prob[0])
    math = lines[-1][end+1]
    print(ans, math, end='')
    for n in range(1, len(prob)):
        if math == '+':
            ans += prob[n]
        elif math == '-':
            ans -= prob[n]
        elif math == '/':
            ans /= prob[n]
        elif math == '*':
            ans *= prob[n]
        if n != len(prob)-1:
            print(prob[n], math, end='')
        else:
            print(prob[n], ' =', ans)
            answer += ans

print('Day 6 Part 2 Answer:', answer)




