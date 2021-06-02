ABCD = input()

for i in range(2**3):

    bin_i = bin(i)[2:]
    bin_i = '{:0=3}'.format(int(bin_i))

    num = int(ABCD[0])
    s = ABCD[0]
    for j in range(len(ABCD)-1):

        if bin_i[j] == '0':
            num -= int(ABCD[j+1])
            s += '-'+ABCD[j+1]
        elif bin_i[j] == '1':
            num += int(ABCD[j+1])
            s += '+'+ABCD[j+1]
    if num == 7:
        print(s+'=7')
        exit()
