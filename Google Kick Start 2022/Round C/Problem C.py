from collections import deque

def ants_on_a_stick():
    N, L = map(int, input().split())
    P, D = [0]*N, [0]*N
    for i in range(N):
        P[i], D[i] = map(int, input().split())
    result = []
    ants = deque(sorted(range(N), key=lambda x: P[x]))
    for p, d in sorted((P[i], D[i]) if not D[i] else (L-P[i], D[i]) for i in range(N)):
        if not d:
            result.append((p, ants.popleft()+1))
        else:
            result.append((p, ants.pop()+1))
    result.sort()
    return " ".join(map(lambda x:str(x[1]), result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, ants_on_a_stick()))