def encode(n, x):
    code = ['-' if x == '.' else '.', x]
    result = [code[0]]*(n+1)
    result.append(code[1])
    return "".join(result)

def second_meaning():
    N = int(input())
    S = input()
    result = [encode(i, S[0]) for i in range(N-1)]
    return "\n%s" % "\n".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_meaning()))