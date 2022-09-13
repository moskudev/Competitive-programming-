from collections import Counter

def count(n):
    X_cnt, Y_cnt = Counter(), Counter()
    for _ in range(n):
        X, Y = list(map(int, input().split()))
        X_cnt[X] += 1
        Y_cnt[Y] += 1
    return X_cnt, Y_cnt

def f(X_cnt, A_cnt):
    result = 0
    for X, cntX in X_cnt.items():
        for A, cntA in A_cnt.items():
            result = (result+cntX*cntA*(X-A)**2)%MOD
    return result

def watering_well_chapter_1():
    A_cnt, B_cnt = count(int(input()))
    X_cnt, Y_cnt = count(int(input()))
    return (f(X_cnt, A_cnt)+f(Y_cnt, B_cnt))%MOD

MOD = 10**9+7
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, watering_well_chapter_1()))