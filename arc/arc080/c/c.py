N = int(input())
a = list(map(int, input().split()))

_2a = 0
_4a = 0
_a = 0
for i in range(N):
    if a[i] % 4 == 0:
        _4a += 1

    elif a[i] % 2 == 0:
        _2a += 1

    else:
        _a += 1

if _a+_4a == N and _4a+1 >= _a:
    ans = True

elif _a > _4a:
    ans = False

else:
    ans = True

print('Yes' if ans is True else 'No')
