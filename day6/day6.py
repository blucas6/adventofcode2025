answer = 0
problems = []
lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

for ix,line in enumerate(lines):
    problems.append(line.split())

for c in range(len(problems[0])):
    ans = int(problems[0][c])
    math = problems[-1][c]
    print(ans, math, end=' ')
    for n in range(1, len(problems)-1):
        print(problems[n][c], math, end=' ')
        num = int(problems[n][c])
        if math == '+':
            ans += num
        elif math == '-':
            ans -= num
        elif math == '/':
            ans /= num
        elif math == '*':
            ans *= num
    print('=', ans)
    answer += ans

print('Day 6 Answer Part 1:', answer)


