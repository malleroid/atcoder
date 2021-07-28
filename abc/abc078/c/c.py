N, M = map(int, input().split())

num = 100*(N-M)+1900*M
ans = num*2**M

print(ans)
