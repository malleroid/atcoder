S = input()
Q = int(input())

t = 0
before = ''
after = ''
for i in range(Q):
    q = input()
    T = q[0]

    if T == '1':
        t += 1

    else:
        t %= 2

        F = int(q[2])
        C = q[4]

        if (t+F) % 2 == 0:
            after += C

        else:
            before += C

before = before[::-1]
ans = before+S+after

if t % 2 == 1:
    ans = ans[::-1]

print(ans)
