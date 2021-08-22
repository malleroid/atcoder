L, R = map(int, input().split())

mod = 10**9+7

len_l = len(str(L))
len_r = len(str(R))

ans = 0
for i in range(len_l, len_r+1):
    num_l = 10**(i-1)-1
    num_r = 10**i-1
    if i == len_l:
        num_l = L-1

    if i == len_r:
        num_r = R

    ans += ((num_r*(num_r+1)//2)-(num_l*(num_l+1)//2))*i

print(ans % mod)
