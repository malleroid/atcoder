N = int(input())
s = input()

r = s.count('R')
b = s.count('B')

print('Yes' if r > b else 'No')
