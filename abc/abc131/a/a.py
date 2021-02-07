S = input()

ans = True
for i in range(3):
    if S[i] == S[i+1]:
        ans = False
        break

print('Good' if ans is True else 'Bad')
