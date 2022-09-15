def direction(a, b, n):
    r, c = divmod(a, n)
    nr, nc = divmod(b, n)
    if nr-r == 1: return 'S'
    if nc-c == 1: return 'E'
    if nr-r == -1: return 'N'
    if nc-c == -1: return 'W'

def create_node(n, curr, nxts):
    r, c = curr
    r, c = 2*r, 2*c
    if nxts[r*n+c] != -1:
        return False
    for dr, dc in DIRECTIONS:
        nxts[r*n+c] = (r+dr)*n+(c+dc)
        r, c = r+dr, c+dc
    return True

def merge_node(n, curr, parent, nxts):
    if curr < parent:
        curr, parent = parent, curr
    r, c = curr
    pr, pc = parent
    if r-pr:
        nxts[(2*r)*n+(2*c)] = (2*pr+1)*n+(2*c)
        nxts[(2*pr+1)*n+(2*pc+1)] = (2*r)*n+(2*c+1)
    else:
        nxts[(2*r+1)*n+(2*c)] = (2*pr+1)*n+(2*pc+1)
        nxts[(2*pr)*n+(2*pc+1)] = (2*r)*n+(2*c)

def iter_dfs(R, C, B):
    nxts = [-1]*((2*R)*(2*C))
    create_node(2*C, (0, 0), nxts)
    stk = [(1, ((0, 0), None))]
    while stk:
        step, args = stk.pop()
        if step == 1:
            curr, parent = args
            if parent:
                merge_node(2*C, curr, parent, nxts)
            stk.append((2, (curr, 0)))
        elif step == 2:
            curr, i = args
            nr, nc = curr[0]+DIRECTIONS[i][0], curr[1]+DIRECTIONS[i][1]
            if i+1 < len(DIRECTIONS):
                stk.append((2, (curr, i+1)))
            if not (0 <= nr < R and 0 <= nc < C and B[nr][nc] == '*' and create_node(2*C, (nr, nc), nxts)):
                continue
            stk.append((1, ((nr, nc), curr)))
    return nxts

def hamiltonian_tour():
    R, C = map(int, input().split())
    B = [input() for _ in range(R)]
    nxts = iter_dfs(R, C, B)
    if nxts.count(-1) != 4*sum(row.count('#') for row in B):
        return "IMPOSSIBLE"
    result = []
    curr = 0
    while not (result and curr == 0):
        result.append(direction(curr, nxts[curr], 2*C))
        curr = nxts[curr]
    return "".join(result)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, hamiltonian_tour()))