s=input()

if ('N' not in s or 'S' not in s) and ('N' in s or 'S' in s) :
    print('No')    

elif ('E' not in s or 'W' not in s) and ('E' in s or 'W' in s) :
    print('No')

else:
    print('Yes')