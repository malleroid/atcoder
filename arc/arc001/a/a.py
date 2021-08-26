N = int(input())
c = input()

cl = [c.count('1'), c.count('2'), c.count('3'), c.count('4')]

cl.sort()
print(cl[3], cl[0], sep=' ')
