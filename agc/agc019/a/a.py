Q, H, S, D = map(int, input().split())
N = int(input())

S = min(S, 2*H, 4*Q)
D = min(D, 2*S)

ans = D*(N//2) if N % 2 == 0 else D*(N//2)+S

print(ans)
