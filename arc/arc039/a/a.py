A, B = map(int, input().split())

num = A-B

for i in range(3):
    a = list(str(A))
    a[i] = '9'
    a = int(''.join(a))

    if a-B > num:
        num = a-B

for i in range(3):
    b = list(str(B))
    b[i] = '0' if i != 0 else '1'
    b = int(''.join(b))

    if A-b > num:
        num = A-b

print(num)
