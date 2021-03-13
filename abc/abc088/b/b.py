n = int(input())
a = list(map(int, input().split()))

a.sort()
a.reverse()

alice_arr = a[0::2]
bob_arr = a[1::2]

alice_num = sum(alice_arr)
bob_num = sum(bob_arr)

print(alice_num-bob_num)
