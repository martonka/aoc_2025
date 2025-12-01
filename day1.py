#/usr/bin/env python3

import sys
import math

data = sys.stdin.read() 
v = 50
res = 0
for l in data.splitlines():
    l = l.strip().lower()
    if not l:
        continue
    
    if l.startswith("l"):
        v -= int(l[1:])
    if l.startswith("r"):
        v += int(l[1:])
    
    v = v % 100
    
    if v == 0:
        res += 1

print("P1:", res)

v = 50
res = 0
for l in data.splitlines():
    l = l.strip().lower()
    if not l:
        continue
    
    if l.startswith("l"):
        if v == 0:
            res -= 1
        v -= int(l[1:])
        res -= math.floor((v - 1) // 100)
    if l.startswith("r"):
        v += int(l[1:])
        res += math.floor(v // 100)

    v = v % 100

print("P2:", res)
