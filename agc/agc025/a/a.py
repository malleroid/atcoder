N = int(input())

if N % 10 == 0:
    print(10)

else:

    ans = sum(list(map(int, str(N))))
    print(ans)
