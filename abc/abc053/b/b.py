s = input()

a = s.index('A')

for i in range(len(s)):

    if s[len(s)-i-1] == 'Z':
        z = len(s)-i
        break

print(z-a)
