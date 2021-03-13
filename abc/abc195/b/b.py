A, B, W = map(int, input().split())

W = W*1000

max_num = W//A
min_num = W//B if W % B == 0 else W//B+1

if min_num > max_num:
    print('UNSATISFIABLE')
elif min_num == max_num:
    print(max_num, max_num, sep=' ')
else:
    print(min_num, max_num, sep=' ')
