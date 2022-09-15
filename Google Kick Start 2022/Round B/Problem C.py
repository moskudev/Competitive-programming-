def unlock_the_padlock():
    def memoization(left, right, x, lookup):  # use lookup instead of lru_cache which results in MLE in Python3
        if (left, right, x) not in lookup:
            lookup[left, right, x] = min((memoization(left+1, right, V[left], lookup) if left+1 <= right else 0) + min((V[left]-x)%D, D-(V[left]-x)%D),
                                         (memoization(left, right-1, V[right], lookup) if left <= right-1 else 0) + min((V[right]-x)%D, D-(V[right]-x)%D))
        return lookup[left, right, x]

    N, D = map(int, input().split())
    V = list(map(int, input().split()))
    return memoization(0, N-1, 0, {})

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, unlock_the_padlock()))