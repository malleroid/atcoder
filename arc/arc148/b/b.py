N = int(input())
S = input()

bool_S = [1 if s == "d" else 0 for s in S]

if 0 not in bool_S:
    print(S)
    exit()

first_zero_index = bool_S.index(0)

rotate_target = bool_S[first_zero_index:]

rotated_list = []

for i in range(len(rotate_target)):
    if rotate_target[i] == 1:
        continue

    left = rotate_target[:i+1][::-1]
    right = rotate_target[i+1:]
    for j in range(i+1):
        left[j] ^= 1

    rotated_list.append(''.join([str(n) for n in left+right]))

rotated_list.sort(reverse=True)

reverted_alpha = ["d" if s == "1" else "p" for s in rotated_list[0]]

print(S[:first_zero_index] + ''.join(reverted_alpha))
