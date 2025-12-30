invalidids = 0
with open('day2input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        ranges = line.split(',')
        for rang in ranges:
            rang = rang.strip()
            if not rang:
                continue
            start = int(rang.split('-')[0])
            end = int(rang.split('-')[1])
            for n in range(start, end+1):
                n = str(n)
                if len(n) % 2 == 0:
                    mid = round((len(n) / 2))
                    if n[:mid] == n[mid:]:
                        invalidids += int(n)
print(f'Day 2 Part 1 Answer: {invalidids}')

invalidids = 0
with open('day2input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        ranges = line.split(',')
        for rang in ranges:
            rang = rang.strip()
            if not rang:
                continue
            start = int(rang.split('-')[0])
            end = int(rang.split('-')[1])
            for n in range(start, end+1):
                n = str(n)
                sub = ''
                invalid = -1
                for ch in n:
                    sub += ch
                    if len(sub) > len(n) / 2:
                        break
                    if len(n) % len(sub) != 0:
                        continue
                    good = True
                    for ind in range(len(sub), len(n), len(sub)):
                        if sub != n[ind:ind+len(sub)]:
                            good = False
                            break
                    if good:
                        invalid = int(n)
                if invalid != -1:
                    invalidids += invalid
print(f'Day 2 Part 2 Answer: {invalidids}')
