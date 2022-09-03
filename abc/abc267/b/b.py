S = input()

if S[0] == '1':
    print('No')
    exit()

l1 = S[6]
l2 = S[3]
l3 = S[1]+S[7]
l4 = S[0]+S[4]
l5 = S[2]+S[8]
l6 = S[5]
l7 = S[9]
pins = [l1, l2, l3, l4, l5, l6, l7]

reserved_pins = ''

for i in range(7):
    cnt = pins[i].count('1')
    reserved_pins += '1' if cnt > 0 else '0'

a = reserved_pins.find('1')

if a == -1:
    print('No')
    exit()

b = reserved_pins.find('0', a+1)

if b == -1:
    print('No')
    exit()

c = reserved_pins.find('1', b+1)

if c == -1:
    print('No')
else:
    print('Yes')
