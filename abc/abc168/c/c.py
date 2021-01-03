import numpy as np

a, b, h, m = map(int, input().split())

# 時針は1時間で 30°回る , 1分で 0.5°回る
# 分針は1分で 6°回る

# +90°- Θ

# 時針
hour = np.array([a*np.cos(np.radians(90)-(np.radians(30*h)+np.radians(0.5*m))), a*np.sin(np.radians(90)-(np.radians(30*h)+np.radians(0.5*m)))])

minute = np.array([b*np.cos(np.radians(90)-(np.radians(6*m))), b*np.sin(np.radians(90)-(np.radians(6*m)))])

diff = hour - minute

print(np.linalg.norm(diff))