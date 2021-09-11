import numpy as np

N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

s = np.array(S)
t = np.array(T)

s_col = np.count_nonzero(s == '#', axis=0)
s_row = np.count_nonzero(s == '#', axis=1)
t_col = np.count_nonzero(t == '#', axis=0)
t_row = np.count_nonzero(t == '#', axis=1)

i = 1
while True:
    if s_row[N-i] == 0:
        s = np.delete(s, N-i, 0)
        i += 1
    else:
        break

i = 0
while True:
    if s_row[i] == 0:
        s = np.delete(s, 0, 0)
        i += 1
    else:
        break

i = 1
while True:
    if s_col[N-i] == 0:
        s = np.delete(s, N-i, 1)
        i += 1
    else:
        break

i = 0
while True:
    if s_col[i] == 0:
        s = np.delete(s, 0, 1)
        i += 1
    else:
        break

i = 1
while True:
    if t_row[N-i] == 0:
        t = np.delete(t, N-i, 0)
        i += 1
    else:
        break

i = 0
while True:
    if t_row[i] == 0:
        t = np.delete(t, 0, 0)
        i += 1
    else:
        break

i = 1
while True:
    if t_col[N-i] == 0:
        t = np.delete(t, N-i, 1)
        i += 1
    else:
        break

i = 0
while True:
    if t_col[i] == 0:
        t = np.delete(t, 0, 1)
        i += 1
    else:
        break

for i in range(4):
    s = np.rot90(s)

    if s.shape == t.shape:
        comp = s == t
        if np.all(comp):
            print('Yes')
            exit()

print('No')
