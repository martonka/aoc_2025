#/usr/bin/env python3
import sys
from itertools import combinations

res = 0
res2 = 0
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    mx = 0
    for i, j in combinations(line, 2):
        a, b = int(i), int(j)
        mx = max(mx, a * 10 + b)

    mxs = [0] * 13
    
    for c in line:
        for l in range(12, 0, -1):
            d = int(c)
            mxs[l] = max(mxs[l], 10 * mxs[l - 1] + d)
    
    print(mxs[12])
    res += mx
    res2 += mxs[12]
    
print("P1:", res)
print("P2:", res2)