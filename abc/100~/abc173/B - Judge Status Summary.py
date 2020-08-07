n=int(input())

s=[]
for _ in range(n):
    
    s_n=input()
    s.append(s_n)

ac=s.count('AC')
wa=s.count('WA')
tle=s.count('TLE')
re=s.count('RE')

print('AC x '+str(ac))
print('WA x '+str(wa))
print('TLE x '+str(tle))
print('RE x '+str(re))