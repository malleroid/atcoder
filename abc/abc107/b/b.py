import numpy as np

H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

h = []
for i in range(H):
    if '#' not in a[i]:
        h.append(i)

w = []
for i in range(W):

    fl = True
    for j in range(H):
        if a[j][i] == '#':
            fl = False
            break

    if fl is True:
        w.append(i)

h.sort(reverse=True)
w.sort(reverse=True)

a = np.array(a)
for i in range(len(h)):
    a = np.delete(a, h[i], axis=0)

for i in range(len(w)):
    a = np.delete(a, w[i], axis=1)

for i in range(H-len(h)):
    print(''.join(a[i]))
