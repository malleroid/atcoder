A, B = map(int, input().split())

a = ('0'*8+bin(A)[2:])[-8:]
b = ('0'*8+bin(B)[2:])[-8:]

n = [0]*8
for i in range(8):
    n[i] = str((int(a[i])+int(b[i])) % 2)

n = ''.join(n)

print(int(n, 2))
