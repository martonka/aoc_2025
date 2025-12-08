import sys
from itertools import combinations

res1 = 0
res2 = 0


points = []

for l in sys.stdin:
    l = l.strip()
    if not l:
        continue
    x, y, z = l.split(',')
    points.append((int(x), int(y), int(z)))
    

def p1_edges(points, count):
    s = set()
    rr = []
    for idx1, idx2 in combinations(range(len(points)), 2):
        p1 = points[idx1]
        p2 = points[idx2]
        # straight line distance
        d_square = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2
        rr.append((d_square, idx1, idx2))
    rr.sort()

    edges = {}
    for i in range(len(points)):
        edges[i] = []
    for  _, a, b in rr[:count]:
        edges[a].append(b)
        edges[b].append(a)
    return edges, rr           

def get_scc_sizes(edges):
    n = len(edges)
    visited = [False] * n
    sizes = []

    for start in range(n):
        if not visited[start]:
            # BFS/DFS to count component size
            stack = [start]
            visited[start] = True
            size = 0

            while stack:
                node = stack.pop()
                size += 1
                for nei in edges[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            sizes.append(size)

    return sizes

if len(points) == 1000:
    rs = 1000
else:
    rs = 10    
edges1, rr1 = p1_edges(points, rs)
sizes1 = get_scc_sizes(edges1)
res1 = sorted(sizes1, reverse=True)[:3]
print("Part 1:", res1)
res1 = res1[0] * res1[1] * res1[2]
print("Part 1:", res1)

edges2, rr2 = p1_edges(points, len(points) * (len(points) -1 ) // 2)

def binarySearch(val, rr, low, high):
    while low + 2 < high:
        mid = (low + high)//2
        edges = {}
        for i in range(len(points)):
            edges[i] = []
        for  _, a, b in rr[:mid]:
            edges[a].append(b)
            edges[b].append(a)
        
        print("Testing mid:", mid)
        
        max_group = max(get_scc_sizes(edges))
        print("Max group size:", max_group)
        
        if max_group >= val:
            high = mid + 1
        else:
            low = mid
    return low + 1


res2_idx = binarySearch(len(points), rr2, 0, len(rr2)) -1

p1_idx, p2_idx = rr2[res2_idx][1], rr2[res2_idx][2]

p1, p2 = points[p1_idx], points[p2_idx]

print("Part 2:", p1[0], p2[0], p1[0] * p2[0])