S = input()
k = 26
origin = ord('a')

for i in range(k):

    if chr(origin+i) not in S:
        print(chr(origin+i))
        exit()

print('None')
