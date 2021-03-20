N, K = map(int, input().split())

mod = N % K

print(mod if mod <= abs(mod-K) else abs(mod-K))
