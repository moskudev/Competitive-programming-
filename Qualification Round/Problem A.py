from collections import Counter

def second_hands():
    N, K = map(int, input().split())
    S = map(int, input().split())
    return "YES" if N <= 2*K and max(Counter(S).values()) <= 2 else "NO"

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_hands()))