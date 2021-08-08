A, B, X = map(int, input().split())

top = pow(10, 9)
bot = 0

while True:

    mid = (top+bot)//2
    if A*mid+B*len(str(mid)) < X:
        bot = mid

    else:
        top = mid

    if top-bot == 1:
        num = top if A*top+B*len(str(top)) <= X else bot
        break


print(num)
