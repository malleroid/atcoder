A, B, C, D = map(int, input().split())

if C < A or (A == C and D < B):
    print("Aoki")
else:
    print("Takahashi")
