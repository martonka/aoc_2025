import sys

ranges = []
prods = []

for l in sys.stdin:
    l = l.strip()
    if not l:
        continue
    
    if '-' in l:
        a, b = l.split('-')
        ranges.append((int(a), int(b)))
    else:
        prods.append(int(l))


res1 = 0
res2 = 0

for p in prods:
    for r in ranges:
        a, b = r
        if a <= p <= b:
            res1 += 1
            break

ranges = sorted(ranges)

i = 0
while i < len(ranges) - 1:
    for j in range(i + 1, len(ranges)):
        a1, b1 = ranges[i]
        a2, b2 = ranges[j]
        
        if b1 + 1 < a2:
            break
        
        na = min(a1, a2)
        nb = max(b1, b2)
        
        ranges[i] = (na, nb)
        ranges[j] = (-1, -1)
    ranges = [r for r in ranges if r != (-1, -1)]
    i += 1

for r in ranges:
    a, b = r
    res2 += b - a + 1

print("Part 1:", res1)
print("Part 2:", res2)