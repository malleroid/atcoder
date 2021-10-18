import heapq

N = int(input())

n = ord('a')

indeg = [0]*26
outdeg = {i: [] for i in range(26)}

for _ in range(N):
    A, B = input().split()

    flg = False
    for i in range(min(len(A), len(B))):
        if A[i] != B[i]:
            indeg[ord(B[i])-n] += 1
            outdeg[ord(A[i])-n].append(ord(B[i])-n)
            flg = True
            break

    if flg is False and len(A) > len(B):
        print(-1)
        exit()

q = []
heapq.heapify(q)

for i in range(26):
    if indeg[i] == 0:
        heapq.heappush(q, i)

ans = []
while q:
    p = heapq.heappop(q)
    ans.append(chr(p+n))

    for e in outdeg[p]:
        indeg[e] -= 1
        if indeg[e] == 0:
            heapq.heappush(q, e)

if len(ans) != 26:
    print(-1)

else:
    print(*ans, sep='')
