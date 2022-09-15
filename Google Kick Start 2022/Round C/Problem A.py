from string import ascii_lowercase, ascii_uppercase

def new_password():
    N = int(input())
    P = list(input())
    result = P[:]
    for requirement in (UPPER, LOWER, DIGIT, SPECIAL):
        if not any(x in requirement for x in P):
            result.append(next(iter(requirement)))
    result.append(next(iter(UPPER))*(L-len(result)))
    return "".join(result)

L = 7
UPPER = set(ascii_uppercase)
LOWER = set(ascii_lowercase)
DIGIT = set(str(i) for i in range(10))
SPECIAL = set("#@*&")
for case in range(int(input())):
    print('Case #%d: %s' % (case+1, new_password()))
