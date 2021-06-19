import math

R, X, Y = map(int, input().split())

print(2 if math.sqrt(X**2+Y**2) < R else math.ceil(math.sqrt(X**2+Y**2)/R))
