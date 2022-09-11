def ceil_divide(a, b):
    return (a+b-1)//b

def coloring_game():
    N = int(input())
    return ceil_divide(N, 5)

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, coloring_game()))