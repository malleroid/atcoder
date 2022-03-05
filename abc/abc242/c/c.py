import copy

N = int(input())

mod = 998244353

now_array = [0]*9
prev_array = [0]*9

for i in range(N):
    prev_array = copy.deepcopy(now_array)
    now_array = [0]*9
    for j in range(9):
        if i == 0:
            now_array[j] = 1

        else:
            if j == 0:
                now_array[j] = (prev_array[j]+prev_array[j+1]) % mod

            elif j == 8:
                now_array[j] = (prev_array[j-1]+prev_array[j]) % mod

            else:
                now_array[j] = (prev_array[j-1]+prev_array[j] +
                                prev_array[j+1]) % mod

print(sum(now_array) % mod)
