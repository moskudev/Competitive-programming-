def z_function(s): 
    z = [0]*len(s)
    l, r = 0, 0
    for i in range(1, len(z)):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        while i+z[i] < len(z) and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l, r = i, i+z[i]-1
    return z

def consecutive_cuts_chapter_2():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    z = z_function(B+A+A)
    for i in range(N):
        if z[i+N] < N:
            continue
        if (N == 2 and K%2 == int(i != 0)) or (N > 2 and K != int(i == 0)):
            return "YES"
    return "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, consecutive_cuts_chapter_2()))