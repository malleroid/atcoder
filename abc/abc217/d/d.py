import array
import bisect

L, Q = map(int, input().split())

v = array.array('i')
n = 0
for i in range(Q):
    c, x = map(int, input().split())

    if c == 1:
        bisect.insort_left(v, x)
        n += 1

    else:
        if n == 0:
            print(L)

        else:
            p = bisect.bisect_left(v, x)
            if p == 0:
                print(v[0])
            elif p == n:
                print(L-v[p-1])
            else:
                print(v[p]-v[p-1])
