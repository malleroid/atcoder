N = input()

n = N.replace('0', '')

print('Yes' if (N[-1] == '0' and n == n[::-1]) or N == N[::-1] else 'No')
