import re

s=input()

s=re.sub(r"\D", "",s)

print(s)