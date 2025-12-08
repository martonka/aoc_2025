import sys


beams = None

res0 = 0

for l in sys.stdin:
    l = l.strip('\n')
    if not l:
        continue

    if beams is None:
        beams = [0] * len(l)
        
    beams2 = [0] * len(l)
    
    for i, ch in enumerate(l):
        if ch == 'S':
            beams2[i] += 1
        if ch == '^':
            if beams[i] > 0:
                res0 += 1
            beams2[i-1] += beams[i]
            beams2[i+1] += beams[i]
        if ch == '.':
            beams2[i] += beams[i]
    
    beams = beams2
    
res1 = sum(beams)
print("Part 1:", res1)
print("Part 0:", res0)