A, B = map(int, input().split())

print(B-A if (A > 0 and B > 0) or (A < 0 and B < 0) else B-A-1)
