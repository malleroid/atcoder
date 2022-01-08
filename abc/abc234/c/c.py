K = int(input())

bin_k = bin(K)[2:]

ans = bin_k.replace('1', '2')

print(ans)
