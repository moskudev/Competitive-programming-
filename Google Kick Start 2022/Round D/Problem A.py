def image_labeler():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A.sort()
    return (A[(0+((N-(M-1))-1))//2] if (N-(M-1))%2 else (A[(0+((N-(M-1))-1))//2]+A[(0+((N-(M-1))-1))//2+1])/2.0) + sum(A[~i] for i in range(M-1))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, image_labeler()))