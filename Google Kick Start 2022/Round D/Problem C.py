def touchbar_typing():
    N = int(input())
    S = list(map(int, input().split()))
    M = int(input())
    K = list(map(int, input().split()))
    lookup = set(S)
    neis = [{}, {}]
    for idx, rng in enumerate([range(M), reversed(range(M))]):
        nei = neis[idx]
        curr = {}
        for i in rng:
            if K[i] not in lookup:
                continue
            curr[K[i]] = i
            nei[i] = {j:x for j, x in curr.items()}
    dp = {i:0 for i in range(M) if K[i] in lookup}
    for x in S:
        new_dp = {}
        for i, d in dp.items():
            for nei in [neis[0][i], neis[1][i]]:
                if x not in nei:
                    continue
                j = nei[x]
                if j not in new_dp or new_dp[j] > d+abs(j-i):
                    new_dp[j] = d+abs(j-i)
        dp = new_dp
    return min(dp.values())

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, touchbar_typing()))