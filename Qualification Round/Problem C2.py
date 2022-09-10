def encode(n, x, l):
    code = ['-' if x == '.' else '.', x]
    result = []
    for i in reversed(range(l)):
        result.append(code[(n>>i)&1])
    return "".join(result)

def second_second_meaning():
    N = int(input())
    S = input()
    ceil_log2_N = (N-1).bit_length()
    result = [encode(i, S[0], ceil_log2_N+1) for i in range(N-1)]
    return "\n%s" % "\n".join(result)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_second_meaning()))