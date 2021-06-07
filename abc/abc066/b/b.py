S = input()

S = S[:-1]

while len(S) > 0:

    if len(S) % 2 != 0:
        S = S[:-1]

    half = len(S)//2
    left = S[:half]
    right = S[half:]

    if left == right:
        print(len(S))
        exit()

    S = S[:-2]
