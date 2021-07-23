H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]

num = 0
for i in range(H):
    num += A[i].count('#')

print('Possible' if num == H+W-1 else 'Impossible')
