def inv_nCr(n, k):
    while len(INV) <= n:
        FACT.append(FACT[-1]*len(INV) % MOD)
        INV.append(INV[MOD%len(INV)]*(MOD-MOD//len(INV)) % MOD)
        INV_FACT.append(INV_FACT[-1]*INV[-1] % MOD)
    return (INV_FACT[n]*FACT[n-k] % MOD) * FACT[k] % MOD

def palindromic_deletions():
    N = int(input())
    S = input()
    result = 1
    dp = [[[0]*N for _ in range(N)] for _ in range(L)]  # dp[l%L][i][j]: number of palindromes of length l in the substring of S[i, j]
    for l in range(1, N):
        for i in reversed(range(N)):
            dp[l%L][i][i] = (1 if l == 1 else 0)
            for j in range(i+1, N):
                dp[l%L][i][j] = (dp[l%L][i+1][j]+dp[l%L][i][j-1]-dp[l%L][i+1][j-1])%MOD  # inclusion-exclusion principle
                if S[i] == S[j]:
                    dp[l%L][i][j] = (dp[l%L][i][j]+(1 if l == 2 else dp[(l-2)%L][i+1][j-1]))%MOD
        result = (result+dp[l%L][0][N-1]*inv_nCr(N, l))%MOD
    return result

L = 3
MOD = 10**9+7
FACT, INV, INV_FACT = [[1]*2 for _ in range(3)]
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindromic_deletions()))