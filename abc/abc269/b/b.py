S = [input() for _ in range(10)]

is_found = False
for i in range(10):
    if is_found:
        break

    for j in range(10):
        if is_found:
            break
        if S[i][j] == '#':
            A, C = i+1, j+1
            is_found = True

is_found = False
for i in range(10):
    if is_found:
        break

    for j in range(10):
        if S[9-i][9-j] == '#':
            B, D = 9-i+1, 9-j+1
            is_found = True
            break

print(A, B)
print(C, D)
