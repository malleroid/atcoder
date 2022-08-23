N = int(input())
S = input()

ans = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            i_index = S.find(str(i))

            if i_index == -1:
                continue

            j_index = S[i_index+1:].find(str(j))

            if j_index == -1:
                continue

            k_index = S[i_index+j_index+2:].find(str(k))

            if k_index == -1:
                continue

            ans += 1

print(ans)
