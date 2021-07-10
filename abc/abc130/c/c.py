W, H, x, y = map(int, input().split())

flag = 1 if x*2 == W and y*2 == H else 0
print(W*H/2, flag, sep=' ')
