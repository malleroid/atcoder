# コーナーケース
H, W = map(int, input().split())

ans = 0

if H == 1 or W == 1:
    ans = H*W

else:

    h = (H+1)//2
    w = (W+1)//2
    ans = h*w

print(ans)
