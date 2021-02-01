S = input()

s = S.replace('eraser', '').replace('erase', '').replace(
    'dreamer', '').replace('dream', '')

print('YES' if s == '' else 'NO')
