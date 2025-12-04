import sys


data = [list(l.strip()) for l in sys.stdin if l.strip()]


def get_value(p):
    x, y = p
    if x < 0 or y < 0:
        return False
    if y >= len(data) or x >= len(data[0]):
        return False
    return data[y][x] == "@"

res1 = 0

def get_all():
    res = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            if not get_value((x, y)):
                continue
            
            cc = 0
            
            for x2 in range(x - 1, x + 2):
                for y2 in range(y - 1, y + 2):
                    if x2 == x and y2 == y:
                        continue
                    if get_value((x2, y2)):
                        cc += 1

            if cc < 4:
                res.append((x, y))
    return res

print("Part 1:", len(get_all()))

res2 = 0

while True:
    points = get_all()
    if not points:
        break
    for p in points:
        res2 += 1
        x, y = p
        data[y][x] = 'x'
        
print("Part 2:", res2)