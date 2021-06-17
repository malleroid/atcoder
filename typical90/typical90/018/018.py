# 3次元幾何学
import math
import numpy as np

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())


for i in range(Q):

    E = int(input())

    rad = 2*math.pi*E/T
    y = -math.cos(rad-math.pi/2)*L/2
    z = math.sin(rad-math.pi/2)*L/2+L/2

    p = np.array([0, y, z])
    q = np.array([X, Y, 0])

    d = np.linalg.norm(q-p)

    print(math.degrees(math.asin(z/d)))
