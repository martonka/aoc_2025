import sys


data = []
data2 = []

for l in sys.stdin:
    l = l.strip('\n')
    if not l:
        continue
    
    parts = l.split()
    data.append(parts)
    data2.append(l)    
# transpose 2d data
data = list(zip(*data))
rr_all = 0
for x in data:
    m = x[-1]
    rr = None
    if m == '+':
        rr = sum(int(v) for v in x[:-1])
    elif m == '*':
        rr = 1
        for v in x[:-1]:
            rr *= int(v)
    
    rr_all += rr

positions = []    
l2 = data2[-1]

for i, ch in enumerate(l2):
    if ch != ' ':
        positions.append(i)
positions.append(len(l2))

rr_all2 = 0
for idx in range(len(positions) - 1):
    start = positions[idx]
    end = positions[idx + 1]
    l_num = len(data2) - 1
    nums = [] 
    for i in range(end-1, start-1, -1):
        n = None
        for j in range(l_num):
            if data2[j][i] != ' ':
                if n is None:
                    n = 0
                n *= 10
                n += int(data2[j][i])
        if n is not None:
            nums.append(n)    
    rr = None
    if data[idx][-1] == '+':
        rr = sum(nums)
    elif data[idx][-1] == '*':
        rr = 1
        for v in nums:
            rr *= v
    print(f"Column {idx+1} result: {rr}")
    rr_all2 += rr 
    
print("Part 1:", rr_all)
print("Part 2:", rr_all2)