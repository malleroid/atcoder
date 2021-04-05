H, W = map(int, input().split())

A = ['#'*(W+2)]

for i in range(H):
    a = '#'+input()+'#'
    A.append(a)

A.append('#'*(W+2))

print('\n'.join(A))
