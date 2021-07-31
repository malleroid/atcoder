X = input()

if len(set(X)) == 1:
    print('Weak')

else:
    for i in range(3):
        if str(int(X[i])+1)[-1] != str(int(X[i+1])):
            print('Strong')
            exit()

    print('Weak')
