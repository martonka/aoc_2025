import sys
from collections import deque

edges = {}

for l in sys.stdin:
    l = l.strip('\n')
    if not l:
        continue

    nn = l.split()
    
    x = nn[0][:-1]
    nn = nn[1:]
    
    edges[x] = nn
   
edges["out"] = []

def order(edges):
    res = []
    count = {}
    for x, es in edges.items():
        if x not in count:
            count[x] = 0
        for e in es:
            
            if e not in count:
                count[e] = 0
            
            count[e] += 1
           
    
    hot =  deque()
    
    for x, y in count.items():
        if y == 0:
            hot.append(x)
            
    while hot:
        n = hot.popleft()
        res.append(n)
        
        for e in edges.get(n, []):
            count[e] -= 1
            if count[e] == 0:
                hot.append(e)
    return res


ways = {}

ord = order(edges)

for n in ord:
    ways[n] = 0
    


ways["svr"] = 1


names = ["dac", "fft"]

for idx, n in enumerate(ord):
    if n in names:
        for o in ord[idx+1:]:
            ways[o] = 0
    for e in edges.get(n, []):
        ways[e] += ways[n]
        

print("Part 1:", ways["out"]) 