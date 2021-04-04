S = input()

for i in range(26):
    cnt = S.count(chr(97+i))

    if cnt >= 2:
        print('no')
        exit()

else:
    print('yes')
