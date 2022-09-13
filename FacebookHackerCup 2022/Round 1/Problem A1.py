def check(A, B, i):
    return all(A[(i+j)%len(A)] == B[j]for j in range(len(A)))

def consecutive_cuts_chapter_1():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    i = A.index(B[0])
    if check(A, B, i):
        if (N == 2 and K%2 == int(i != 0)) or (N > 2 and K != int(i == 0)):
            return "YES"
    return "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, consecutive_cuts_chapter_1()))