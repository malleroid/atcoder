K, A, B = map(int, input().split())

if A >= B-2:
    print(K+1)

else:
    if K-A <= 0:
        print(K+1)

    else:
        ans = A+(K+1-A)//2*(B-A)+(K+1-A) % 2
        print(ans)
