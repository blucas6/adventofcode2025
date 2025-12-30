def getvalue(a, b):
    return int(str(a)+str(b))

joltage = 0
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for bank in lines:
        max = 0
        bank = bank.strip()
        for ax in range(len(bank)-1):
            for bx in range(ax+1, len(bank)):
                trymax = getvalue(bank[ax], bank[bx])
                if trymax > max:
                    max = trymax
        joltage += max
        print(f'Bank: {bank} Max: {max}')
print(f'Part 1 Answer: {joltage}')
