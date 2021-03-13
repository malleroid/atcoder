H, W = map(int, input().split())

ans = 1
if H == 1 or W == 1:
    print(ans)

else:
    if H % 2 == 0 or W % 2 == 0:
        ans = H*W//2

    else:
        ans = (H*W+1)//2

    print(ans)
