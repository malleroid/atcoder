import math
import numpy as np

N = int(input())
x_0, y_0 = map(int, input().split())
x_h, y_h = map(int, input().split())

r = math.sqrt((x_h-x_0)**2+(y_h-y_0)**2)/2
x_orig = (x_h-x_0)/2+x_0
y_orig = (y_h-y_0)/2+y_0

rot_rad = math.pi/(N/2)

R = np.array([[np.cos(rot_rad), -np.sin(rot_rad)],
              [np.sin(rot_rad), np.cos(rot_rad)]])

u = (x_0-x_orig, y_0-y_orig)

res = np.dot(R, u)

res[0] += x_orig
res[1] += y_orig

print(*res)
