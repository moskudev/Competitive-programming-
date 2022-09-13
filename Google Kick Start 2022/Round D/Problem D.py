def bfs(K, adj, i):
    q = [i]
    lookup = {i}
    while q:
        new_q = []
        for u in q:
            for v in adj[u]:
                if v in lookup:
                    continue
                lookup.add(v)
                if len(lookup) > K:
                    return True
                new_q.append(v)
        q = new_q
    return False

def suspects_and_witnesses():
    N, M, K = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    for _ in range(M):
        A, B = list(map(int, input().split()))
        adj[B-1].append(A-1)
    return sum(bfs(K, adj, i) for i in range(N))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, suspects_and_witnesses()))