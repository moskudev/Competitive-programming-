from bisect import bisect_left

def students_and_mentors():
    N = int(input())
    R = list(map(int, input().split()))
    sorted_R = sorted((r, i) for i, r in enumerate(R))
    result = [-1]*N
    for i, r in enumerate(R):
        j = bisect_left(sorted_R, (2*r+1,))-1
        if j < 0:
            continue
        if sorted_R[j][1] != i:
            result[i] = sorted_R[j][0]
        elif j-1 >= 0:
            result[i] = sorted_R[j-1][0]
    return " ".join(map(str, result))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, students_and_mentors()))