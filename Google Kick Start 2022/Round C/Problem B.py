def range_partition():
    N, X, Y = map(int, input().split())
    total = sum(x for x in range(1, N+1))
    q, r = divmod(total, X+Y)
    if r:
        return "IMPOSSIBLE"
    target = q*X
    result = []
    for x in reversed(range(1, N+1)):
        if x > target:
            continue
        target -= x
        result.append(x)
        if not target:
            break
    return "POSSIBLE\n%s\n%s" % (len(result), " ".join(map(str, result)))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, range_partition()))