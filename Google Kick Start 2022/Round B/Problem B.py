def is_palindrome(x):
    y, n = 0, x
    while n:
        n, r = divmod(n, 10)
        y = y*10+r
    return x == y

def palindromic_factors():
    A = int(input())
    result = 0
    curr = 1
    while curr*curr <= A:
        if A%curr == 0:
             result += is_palindrome(curr)
             if A//curr != curr:
                 result += is_palindrome(A//curr)
        curr += 1
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, palindromic_factors()))