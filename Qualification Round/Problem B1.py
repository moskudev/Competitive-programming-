def second_friend():
    R, C = map(int, input().split())
    grid = [list(input()) for _ in range(R)]
    if min(R, C) == 1 and any(x == '^' for row in grid for x in row):
        return "Impossible"
    x = '.' if min(R, C) == 1 else '^'
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] = x
    return "Possible\n%s" % "\n".join(map(lambda x: "".join(x), grid))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, second_friend()))