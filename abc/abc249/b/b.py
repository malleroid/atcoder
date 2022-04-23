import re

S = input()

set_S = set(S)

cap_flag = re.search('[^A-Z]', S)
lower_flag = re.search('[^a-z]', S)

if not cap_flag or not lower_flag:
    print('No')
    exit()

print('Yes' if len(set_S) == len(S) else 'No')
