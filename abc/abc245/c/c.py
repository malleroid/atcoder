N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

current_nums = set()
current_nums.add(A[0])
current_nums.add(B[0])

for i in range(1, N):
    next_nums = set()

    a = A[i]
    b = B[i]

    for num in list(current_nums):
        current_nums.discard(num)
        if abs(num-a) <= K:
            next_nums.add(a)

        if abs(num-b) <= K:
            next_nums.add(b)

    current_nums = next_nums
    if len(current_nums) == 0:
        print("No")
        exit()

print("Yes")
