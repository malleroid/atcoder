def palindrome(matrix, n):
    for i in range(n/2):
        print('')

n = int(input())

mat = []

for i in range(n):
    
    s = list(input())
    mat.append(s)

res = palindrome(mat, n)