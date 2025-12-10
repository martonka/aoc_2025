import sys
from pprint import pprint
import numpy as np
import pulp


machines = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split(' ')
    
    req = parts[0][1:-1]
    
    switch = []
    
    for s in parts[1:-1]:
        s = s.strip("()").split(',')
        ll = list(map(int, s))
        switch.append(ll)
        
    jolt = parts[-1].strip('{}').split(',')
    jolt = list(map(int, jolt))
    
    machines.append((req, switch, jolt))       
    
def combine(state, switch):
    state2 = list(state)
    for idx in switch:
        if state2[idx] == '.':
            state2[idx] = '#'
        else:
            state2[idx] = '.'
    return "".join(state2)
    
    
res1 = 0
for req, switch, jolt in machines:
    init = "." * len(req)
    
    alma = {}
    alma[init] = 0
    
    while True:
        alma2 = {}
        for x in switch:
            for state, count in alma.items():
                state2 = combine(state, x)
                if state2 not in alma:
                    alma2[state2] = count + 1
                    
        if not alma2:
            break
        
        alma.update(alma2)
    
    rr = alma.get(req, None)
    if rr is None:
        raise Exception("Unexpected")
    print("Machine request:", rr)
    res1 += rr 
        
pprint(res1)
         


def combine2(state, switch, limit):
    state2 = list(state)
    for idx in switch:
        state2[idx] += 1
        if state2[idx] > limit[idx]:
            return None
    return tuple(state2)
                
res2 = 0
for req, switch, jolt in machines:

    init = tuple([0] * len(req))
    

    # Coefficient matri
    ll = [[0] * len(jolt) for _ in range(len(switch))]
    for i, s in enumerate(switch):
        for idx in s:
            ll[i][idx] = 1
    A = np.array(ll)
    A = A.transpose()

    c = np.array([1] * len(switch))
    b = np.array(jolt)
    
    m, n = A.shape 
    # Create ILP problem
    problem = pulp.LpProblem("Matrix_ILP", pulp.LpMinimize)

    # Create integer variable vector automatically
    x = pulp.LpVariable.dicts(
        'x',
        indices=range(n),
        lowBound=0,
        upBound=1000000,
        cat='Integer'
    )

    # Objective: c^T x
    problem += pulp.lpSum(c[j] * x[j] for j in range(n))

    # Add constraints: A[i] * x == b[i]
    for i in range(m):
        problem += pulp.lpSum(A[i, j] * x[j] for j in range(n)) == b[i]

    # Solve
    status = problem.solve()

    # Print solution
    if pulp.LpStatus[status] == 'Optimal':
        sol = np.array([x[j].value() for j in range(n)])
        res2 += int(sol.sum())
    else:
        x = np.linalg.pinv(A) @ b
     
        
pprint(res2)
        
    
    