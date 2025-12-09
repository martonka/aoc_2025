import sys
from itertools import combinations, pairwise


points = [] 

for l in sys.stdin:
    l = l.strip()
    if not l:
        continue
    x, y = l.split(',')
    x = int(x)
    y = int(y)
    points.append((x, y))
    
res1 = 0

for p1, p2 in combinations(points, 2):
    area = (abs(p1[0] - p2[0]) + 1)  * (abs(p1[1] - p2[1]) + 1)
    res1 = max(res1, area)

print("Part 1:", res1)


points.append(points[0])

def crosses(tl, br):
    
    for p3, p4 in pairwise(points):
        
        tl_2 = (min(p3[0], p4[0]), min(p3[1], p4[1]))
        br_2 = (max(p3[0], p4[0]), max(p3[1], p4[1]))
        
        h_2 = tl_2[1] == br_2[1]
        
        if h_2:
            
            if tl_2[1] <= tl[1] or tl_2[1] >= br[1]:
                continue
            
            if br_2[0] > tl[0] and tl_2[0] < br[0]: 
                return True
        else:
            if tl_2[0] <= tl[0] or tl_2[0] >= br[0]:
                continue
            if br_2[1] > tl[1] and tl_2[1] < br[1]: 
                return True

    return False

res_2 = 0
   
idx = 0  
n_idx = 1
 
for p1, p2 in combinations(points, 2):
    idx += 1
    if idx == n_idx:
        n_idx *= 2
        print(f"Progress: {idx} / {len(points)*(len(points)-1)//2}")
    
    x1, y1 = p1
    x2, y2 = p2
    
    min_p = min(x1, x2), min(y1, y2)
    max_p = max(x1, x2), max(y1, y2)

    area = (max_p[0] - min_p[0] + 1) * (max_p[1] - min_p[1] + 1)
    
    if crosses(min_p, max_p):
        continue

    if res_2 < area:
        print(f"New max area: {area} from points {p1} and {p2}")
        res_2 = area
    
print("Part 2:", res_2)


