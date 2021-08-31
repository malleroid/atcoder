N, K = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A)

ans = 0
if K >= s:
    for i in range(N):
        ans += A[i]*(A[i]+1)//2

else:
    A.sort(reverse=True)
    A.append(0)

    for i in range(N):

        dif = A[i]-A[i+1]
        if dif*(i+1) <= K:
            ans += (A[i]*(A[i]+1)//2-A[i+1]*(A[i+1]+1)//2)*(i+1)
            K -= dif*(i+1)

        else:
            q = K//(i+1)
            r = K % (i+1)
            ans += (A[i]*(A[i]+1)//2-(A[i]-q)*(A[i]-q+1)//2)*(i+1)
            ans += (A[i]-q)*r
            break

print(ans)
