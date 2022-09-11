def is_palindrome(P, left, right):
    while left < right:
        if P[left] != P[right]:
            return False
        left, right = left+1, right-1
    return True

def matching_palindrome():
    N = int(input())
    P = input()
    l = next(l for l in range(1, len(P)+1) if len(P)%l == 0 and is_palindrome(P, 0, l-1) and is_palindrome(P, l, len(P)-1))
    return P[:l]

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, matching_palindrome()))