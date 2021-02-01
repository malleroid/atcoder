import re

S = input()

print('YES' if re.fullmatch('A?KIHA?BA?RA?', S) else 'NO')
